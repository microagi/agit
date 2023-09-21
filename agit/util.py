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

import subprocess
import textwrap

from colorama import Fore, Style, init
from pyparsing import Literal, Word, alphanums, Optional, ParseException

from agit.logger import mylogger

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


# detect interactive commands
# Define literals for git commands and options
git = Literal("git")
commit = Literal("commit")
rebase = Literal("rebase")
merge = Literal("merge")
tag = Literal("tag")
config = Literal("config")
bisect = Literal("bisect")
stash = Literal("stash")
cherry_pick = Literal("cherry-pick")
var = Literal("var")

# Define literals for options/flags
m = Literal("-m")
no_edit = Literal("--no-edit")
i = Literal("-i")
interactive = Literal("--interactive")
annotate = Literal("-a")
edit = Literal("--edit")

# Interactive commmands.
# Define a word pattern to match command arguments
arg = Word(alphanums + "-_")

# Define the grammar for git commands that launch an interactive editor
commit_command = git + commit + Optional(m + arg)
rebase_command = git + rebase + (i | interactive) + Optional(arg)
merge_command = git + merge + ~no_edit + Optional(arg)
tag_command = git + tag + annotate + ~m + Optional(arg)
config_command = git + config + edit
bisect_command = git + bisect + Literal("run") + Optional(arg)
stash_command = git + stash + (Literal("drop") | Literal("pop")) + Optional(arg)
cherry_pick_command = git + cherry_pick + ~Literal("--no-commit") + Optional(arg)
var_command = git + var + Literal("GIT_EDITOR")

# List of all command grammars
commands = [
    commit_command,
    rebase_command,
    merge_command,
    tag_command,
    config_command,
    bisect_command,
    stash_command,
    cherry_pick_command,
    var_command,
]


def is_interactive_command(cmd_str):
    """
    Checks if the given git command string will launch an interactive editor.

    Parameters:
    cmd_str (str): The git command string to check.

    Returns:
    bool: True if the command will launch an interactive editor, False otherwise.
    """
    for command in commands:
        try:
            # Try to parse the command string using each command grammar
            command.parseString(cmd_str)
            return True
        except ParseException:
            # If parsing fails, try the next command grammar
            continue
    return False
