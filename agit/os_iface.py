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
    if normalized_command_list[0] not in ALLOWED_GIT_COMMANDS:
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
        return ( result.stdout or "")
    except subprocess.CalledProcessError as e:
        return e.stderr
