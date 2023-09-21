# microAGI, AGit Tool is dually licensed:
#
# microAGI tools are open sourced and free to use under GPLv3 in a non-profit
# context (individual, and non-profit endeavors). If you plan to use it in commercial
# setting please contact us at <contact@vitakka.co> for details and pricing.
#
# Our intent with the commercial licensing is primarily to ensure the sustainability
# and ongoing development of the microAGI project. This isn't about imposing hefty licensing
# fees but rather a symbolic contribution to acknowledge the value and effort behind the project.
# As a guideline, we'd appreciate a contribution equivalent to $10 to the project via GitHub Sponsors,
# irrespective of the number of seats you require for using microAGI in your commercial setting.
# Your support helps us continue to provide and improve this tool for everyone!

# The GPLv3 governs individual, non-profit use.
#
# Copyright (C) 2023 Sivan Grünberg <sivan@vitakka.co>
# Vitakka Consulting https://vitakka.co
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
