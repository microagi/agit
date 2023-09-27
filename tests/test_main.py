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

import openai
import pytest
from agit.main import main
from unittest.mock import patch, MagicMock, AsyncMock
from tests import config


@patch("agit.main.argparse.ArgumentParser.parse_args")
@patch("agit.main.translate_to_git_command")
@patch("agit.main.execute_git_command")
@patch("agit.main.is_destructive")
async def test_main_with_translate_command(
    mocked_is_destructive, mocked_execute_git, mocked_translate, mocked_args
):
    # Mocking the return values
    mocked_execute_git.return_value = config.mocked_exec_output
    mocked_args.return_value = MagicMock(
        command=["provide", "current", "status", "of", "the", "repo"],
        debug=True,
        version=False,
        explain=False,
        review=False,
    )
    mocked_translate.return_value = {
        "command": "git status",
        "description": "Provide current status of the repository.",
    }
    mocked_is_destructive.return_value = (False, "non destructive")

    # Set a dummy OpenAI Key
    openai.api_key = "sk-OPENAIDUMMYKEYFORTESTING"
    # Run the main function
    await main()

    # Assertions to ensure correct functions were called
    mocked_translate.assert_awaited_once_with(
        "provide current status of the repo", False
    )

    mocked_is_destructive.assert_called_once_with("git status")
    mocked_execute_git.assert_called_once_with("git status")


@patch("agit.main.argparse.ArgumentParser.parse_args")
@patch("agit.main.review_patch")
async def test_main_with_review(mocked_review, mocked_args):
    # Mocking the return values
    mocked_args.return_value = MagicMock(
        command=[],
        explain=False,
        debug=False,
        review=True,
        version=False,
    )
    mocked_review.return_value = "Looks good!"

    # Run the main function
    await main()

    # Assertions to ensure correct functions were called
    mocked_review.assert_awaited_once()
