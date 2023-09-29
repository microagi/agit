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


from agit.config import DESTRUCTIVE_COMMANDS
from pyparsing import ParseException
import agit.grammar as grammar


# def is_destructive(command):
#     for destructive_command, why in DESTRUCTIVE_COMMANDS.items():
#         if destructive_command in command:
#             return (True, why)
#     return (False, "non destructive")


def is_destructive(cmd_str):
    """
    Checks if the given git command string is potentially destructive.

    Parameters:
    cmd_str (str): The git command string to check.

    """
    for command in grammar.destructive_commands:
        try:
            # Try to parse the command string using each command grammar
            command.parseString(cmd_str)
            scriptalbe_command = " ".join(cmd_str.split()[1:2])
            print(f"scriptable command {scriptalbe_command}")
            return (True, DESTRUCTIVE_COMMANDS[scriptalbe_command])
        except ParseException:
            # If parsing fails, try the next command grammar
            continue
    return (False, "non destructive")