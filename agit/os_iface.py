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


def split_piped_command_string(command_string):
    commands = command_string.split()
    commands = [cmd.strip() for cmd in commands]


    if "|" in commands:
        index = commands.index("|")
        before_pipe = " ".join(commands[:index])
        after_pipe = " ".join(commands[index + 1 :])
        return (before_pipe, after_pipe)
    else:
        return (None, None)


def normalize(command_string: str):
    quoted = quotedString.searchString(command_string)
    quotes = None
    normalized_command_list = None
    if quoted:
        quoted_part = quoted[0][0]
        quotes = quoted_part.split()[0][0]
        command_string = command_string.replace(quoted_part, "")
        normalized_command_list = command_string.split() + [quoted_part.strip(quotes)]
    else:
        normalized_command_list = command_string.split()

    eq_parts = []
    result_list = []
    for part in normalized_command_list:
        if eq_parts:
            result_list[-1] = "".join([eq_parts.pop(), f"{part}"])
        else:
            result_list.append(part)

        if part.endswith("=") or part.endswith(":"):
            eq_parts.append(part)

    normalized_command_list = result_list
    return normalized_command_list


def handle_pipe(command_string: str):
    (cmd1, cmd2) = split_piped_command_string(command_string)
    if cmd1 and cmd2:
        cmd1 = normalize(command_string=cmd1)
        cmd2 = normalize(command_string=cmd2)
        return (cmd1, cmd2)
    else:
        return [normalize(command_string=command_string)]


def authorize(cmd_list):
    if (cmd_list[0] or cmd_list[1]) not in ALLOWED_GIT_COMMANDS:
        return False
    return True


def execute_git_command(command_string: str):
    if not command_string:
        return "Command list is empty."

    interactive = is_interactive_command(command_string)
    normalized_command_list = handle_pipe(command_string)

    # Check if the git command is in the list of allowed commands
    for cmd_list in normalized_command_list:
        if not authorize(cmd_list):
            return f"Command '{cmd_list[0]}' is not allowed."

    # Execute the command
    piped = len(normalized_command_list) > 1
    cmd1_output = None
    result = None
    for idx, cmd_list in enumerate(normalized_command_list):
        if idx == 1:
            try:
                result = subprocess.run(
                    cmd_list,
                    capture_output=not interactive,
                    text=True,
                    check=True,
                    input=cmd1_output,
                )
            except subprocess.CalledProcessError as e:
                return e.stderr
        else:
            try:
                result = subprocess.run(
                    ["git", "-c", "color.ui=always", "-c", "log.decorate=true"]
                    + cmd_list[1:],
                    capture_output=not interactive,
                    text=True,
                    check=True,
                )
            except subprocess.CalledProcessError as e:
                return e.stderr
            cmd1_output = piped and result.stdout
    return result.stdout or ""
