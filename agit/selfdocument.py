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


def explain():
    explanation = """
    AGit is a command-line assistant that translates natural language into Git commands.

    The aim of AGit is to make using Git easier, especially for beginners who might not remember 
    the exact Git commands.

    Basic Usage:
    ------------
    Simply type out what you want to do in natural language, and AGit will translate it into a Git command.
    For example, you might enter:
    $ agit 'compare last two commits'
    And AGit will translate this into: 'git diff HEAD~1 HEAD'

    Safety Measures:
    ----------------
    AGit includes safety measures to prevent the accidental use of destructive Git commands. 
    If a command is deemed potentially destructive (e.g., force pushing, deleting branches, etc.), AGit 
    will ask for user confirmation before proceeding.

    Note: Always ensure you understand what a Git command does before running it. 
    AGit provides a description of the translated command to help with this.

     © 2023 Sivan Grünberg - Vitakka Consulting https://vitakka.co
    """
    print(explanation)
