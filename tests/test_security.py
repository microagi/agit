# Copyright (C) 2023 Sivan Grünberg <sivan@vitakka.co>
# Vitakka Consulting https://vitakka.co
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import pytest
from agit.security import is_destructive


def test_is_destructive():
    # Test a non-destructive command
    result, reason = is_destructive("git status")
    assert not result
    assert reason == "non destructive."

    # Test a destructive command (assuming "git reset --hard" is in DESTRUCTIVE_COMMANDS)
    result, reason = is_destructive("git reset --hard")
    assert result
    assert reason != "non destructive."
