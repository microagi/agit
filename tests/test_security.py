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


import pytest
from agit.security import is_destructive


def test_is_destructive():
    # Test a non-destructive command
    # TODO: Test the new syntactic PEG support by spec'ing complex destructive commands
    result, reason = is_destructive("git status")
    assert not result
    assert reason == "non destructive"

    # Test a destructive command (assuming "git reset --hard" is in DESTRUCTIVE_COMMANDS)
    result, reason = is_destructive("git reset --hard")
    assert result
    assert reason != "non destructive"

    result, reason = is_destructive("git filter-branch --env-filter")
    assert result
    assert reason != "non destructive"

    result, reason = is_destructive("git filter-branch")
    assert result
    assert reason != "non destructive"

    result, reason = is_destructive("git filter-repo")
    assert result
    assert reason != "non destructive"
