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
