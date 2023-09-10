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

import textwrap
from colorama import Fore, Style, init
import subprocess

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
        f"{Fore.LIGHTBLACK_EX}Note: --review is an {Fore.WHITE}experimental{Fore.LIGHTBLACK_EX} feature and may not provide correct results."
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
