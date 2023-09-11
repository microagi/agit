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


def execute_git_command(command_list):
    if not command_list:
        return "Command list is empty."

    # Check if the git command is in the list of allowed commands
    if command_list[0] not in ALLOWED_GIT_COMMANDS:
        return f"Command '{command_list[0]}' is not allowed."

    # Execute the command
    try:
        result = subprocess.run(
            ["git", "-c", "color.ui=always", "-c", "log.decorate=true"]
            + command_list[1:],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
