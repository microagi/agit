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
import textwrap
from colorama import Fore, Style, init
from pyparsing import ParseException

from agit.logger import mylogger
import agit.grammar as grammar

init(autoreset=True)


def print_out(string, out):
    out.write(string + "\n")


def print_explanation(explanation, out):
    separator = f"{Fore.YELLOW}{Style.BRIGHT}{'=' * 50}"
    explanation = textwrap.fill(explanation, width=50)
    print_out(separator, out)
    print_out(f"{Fore.GREEN}AGit Extended Explanation:", out)
    print_out(f"{Fore.WHITE}{explanation}", out)
    print_out(separator, out)


def print_review(feedback, out_stream=None):
    feedback = textwrap.fill(
        feedback,
        fix_sentence_endings=True,
        replace_whitespace=False,
        drop_whitespace=False,
        width=160,
    )
    separator = f"{Fore.YELLOW}{Style.BRIGHT}{'=' * 130}"
    out_stream.write(separator + "\n")
    out_stream.write(f"{Fore.GREEN}AGit Feedback:\n")
    out_stream.write(f"{Fore.WHITE}{feedback}")
    out_stream.write("\n")
    out_stream.write(separator + "\n")
    out_stream.write(
        f"{Fore.LIGHTBLACK_EX}Note: --review is an {Fore.WHITE}experimental{Fore.LIGHTBLACK_EX}"
        " feature and may not provide correct results."
    )


def print_description(description, out):
    description = textwrap.fill(description, width=50)
    print_out(f"{Fore.GREEN}AGit Description> {Fore.WHITE}{description}", out)


def print_command(cmd, out):
    separator = f"{Fore.YELLOW}{Style.BRIGHT}{'-' * 50}"
    command = textwrap.fill(cmd)
    print_out(separator, out)
    print_out(f"{Fore.GREEN}AGit Command> {Fore.WHITE}{command}", out)


def gather_output(cmd: str):
    cmd = cmd.split()
    result = subprocess.run(cmd, capture_output=True, text=True)
    mylogger.debug(f"Execute output: \n {result.stdout}")
    if result.returncode != 0:
        print("Error:", result.stderr)

    return result.stdout


def is_interactive_command(cmd_str):
    """
    Checks if the given git command string will launch an interactive editor.

    Parameters:
    cmd_str (str): The git command string to check.

    Returns:
    bool: True if the command will launch an interactive editor, False otherwise.
    """
    for command in grammar.interactive_commands:
        try:
            # Try to parse the command string using each command grammar
            command.parseString(cmd_str)
            return True
        except ParseException:
            # If parsing fails, try the next command grammar
            continue
    return False
