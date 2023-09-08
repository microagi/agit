# Copyright (C) 2023 Sivan Grünberg <sivan@vitakka.co>
# Vitakka Consulting https://vitakka.co
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import pytest
from agit.openai_api import translate_to_git_command, review_patch
from unittest.mock import patch

# Mocked response for translate_to_git_command
mocked_translation_response = {
    "choices": [
        {
            "message": {
                "content": '{"command": "git status", "description": "Shows the status of changes as untracked, modified, or staged."}'
            }
        }
    ]
}

# Mocked response for review_patch
mocked_review_response = {
    "choices": [
        {
            "message": {
                "content": "The changes look good. Make sure to check the variable names for consistency."
            }
        }
    ]
}


@patch("agit.openai_api.openai.ChatCompletion.acreate")
async def test_translate_to_git_command(mocked_api_call):
    mocked_api_call.return_value = mocked_translation_response
    result = await translate_to_git_command(
        "What's the command to check git status?", False
    )
    assert result == {
        "command": "git status",
        "description": "Shows the status of changes as untracked, modified, or staged.",
    }


@patch("agit.openai_api.openai.ChatCompletion.acreate")
async def test_review_patch(mocked_api_call):
    mocked_api_call.return_value = mocked_review_response
    result = await review_patch("Sample diff content", ["Provide feedback"])
    assert (
        result
        == "The changes look good. Make sure to check the variable names for consistency."
    )
