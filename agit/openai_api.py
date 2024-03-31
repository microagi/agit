# Copyright (C) 2023 Sivan Grünberg <sivan@vitakka.co>
# Vitakka Consulting https://vitakka.co
#
# The microAGI tool AGit is open sourced under GPLv3 license.
#
# If you find it useful, we would greatly appreciate a symbolic contribution to
# acknowledge the value and effort behind the project.
# As a guideline, we'd appreciate a contribution equivalent to $10 via GitHub Sponsors,
# Your support helps us continue to provide and improve this tool for everyone!
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.


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


async def translate_to_git_command(natural_language, explain, context=None):
    explain_instruct = ""
    if explain:
        explain_instruct = (
            " and also an extended explanation of the command, by the key of 'explain'."
        )

    # Serialize the context into a concise summary
    context_summary = ""
    if context:
        # Example: context = {'branches': ['main', 'feature'], 'status': 'clean', ...}
        branches = ", ".join(context.get("branches", [])) + "\n"
        commits = context.get("commits", [])
        item = ""
        result = []
        for commit in commits:
            formatted_items = "\n".join(
                [f"{key}: {value}" for key, value in commit.items()]
            )
            result.append(formatted_items)
        commits_f = "\n\n".join(result)
        status = context.get("status", "Status unknown") + "\n"
        context_summary = (
            f"The current branches are {branches}. "
            f"The commit list is: {commits_f}"
            f"The repository status is {status}. "
        )

    prompt_template = [
        {
            "role": "system",
            "content": f"You are an expert git revision control system mentor, you translate natural language to a "
            f"coherent git command. You will only return commands that are for the git RCS tool and refuse "
            f"commands to other software. You will also return a short description of the command to the user. "
            f"You may also require knowledge about the underlying repository in order to follow the user's query."
            f"In that case, you should base your answers on the provided context, which will contain all sorts"
            f"of information and metadata bout the underlying git repository."
            f"The current repository context: {context_summary}",
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
            temperature=0,
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
            temperature=0.1,
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
