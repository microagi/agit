# microAGI, AGit Tool is dually licensed:
#
# microAGI tools are open sourced and free to use under GPLv3 in a non-profit
# context (individual, and non-profit endeavors). If you plan to use it in commercial
# setting please contact us at <contact@vitakka.co> for details and pricing.
#
# The GPLv3 governs individual, non-profit use.
#
# Copyright (C) 2023 Sivan Grünberg <sivan@vitakka.co>
# Vitakka Consulting https://vitakka.co
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import asyncio
import json
import openai
import os
import tqdm
from dotenv import load_dotenv
from agit.logger import mylogger

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def strip_markdown(text):
    stripped = text.strip("```")
    return stripped


async def translate_to_git_command(natural_language, explain):
    explain_instruct = ""
    if explain:
        explain_instruct = (
            "and also an extended explanation of the command, by the key of 'explain'."
        )
    prompt_template = [
        {
            "role": "system",
            "content": "You are an expert git revision control system mentor, you translate natural language to a "
            "coherent git command. You will only return commands that are for the git RCS tool and refuse "
            "commands to other software."
            f"You will also return short description of the command to the user.",
        },
        {
            "role": "user",
            "content": f"Please return the response in JSON format, with the key 'command' pointing at "
            f"the command, the key 'description' pointing to the"
            f"short description of the command:```{natural_language}```"
            f"{explain_instruct}",
        },
    ]
    task = asyncio.create_task(
        openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo-16k",
            messages=prompt_template,
            temperature=0.2,
        )
    )
    with tqdm.tqdm(
        total=100, desc="Processing", bar_format="{desc}: {elapsed}"
    ) as pbar:
        while not task.done():
            await asyncio.sleep(0)  # Simulate waiting
            pbar.update(10)  # Update without changing progress to refresh spinner
    response = task.result()
    git_command_response = response["choices"][0]["message"]["content"]
    git_command_response = strip_markdown(git_command_response)
    git_command = json.loads(git_command_response)
    return git_command


async def review_patch(diff_content, instruct_review):
    prompt_template = [
        {
            "role": "system",
            "content": """You are an expert developer turned code reviewer. Using your years of experience
                            you provide feedback, tips and improvement to pull requests your team makes.""",
        },
        {
            "role": "user",
            "content": f"""Patch ```diff\n{diff_content}```\n\n
                    Please review this patch and provide feedback. {" ".join(instruct_review)} \n
                    Your expertise as a code reviewer will help ensure the quality of the code changes""",
        },
    ]

    mylogger.debug(f"PT: {prompt_template}")

    task = asyncio.create_task(
        openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo-16k",
            messages=prompt_template,
            temperature=0.2,
        )
    )
    with tqdm.tqdm(
        total=100, desc="Processing", bar_format="{desc}: {elapsed}"
    ) as pbar:
        while not task.done():
            await asyncio.sleep(0)
            pbar.update(10)
    response = task.result()

    agit_response = response["choices"][0]["message"]["content"]
    return agit_response
