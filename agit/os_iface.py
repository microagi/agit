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

import subprocess
from agit.config import ALLOWED_GIT_COMMANDS
from pyparsing import quotedString
from agit.util import is_interactive_command


def execute_git_command(command_string: str):
    if not command_string:
        return "Command list is empty."

    interactive = is_interactive_command(command_string)
    quoted = quotedString.searchString(command_string)
    quotes = None
    if quoted:
        quoted_part = quoted[0][0]
        quotes = quoted_part.split()[0][0]
        command_string = command_string.replace(quoted_part, "")
        normalized_command_list = command_string.split() + [quoted_part.strip(quotes)]
    else:
        normalized_command_list = command_string.split()
    # Check if the git command is in the list of allowed commands
    if (
        normalized_command_list[0] or normalized_command_list[1]
    ) not in ALLOWED_GIT_COMMANDS:
        return f"Command '{normalized_command_list[0]}' is not allowed."

    # Execute the command
    try:
        result = subprocess.run(
            ["git", "-c", "color.ui=always", "-c", "log.decorate=true"]
            + normalized_command_list[1:],
            capture_output=not interactive,
            text=True,
            check=True,
        )
        return result.stdout or ""
    except subprocess.CalledProcessError as e:
        return e.stderr
