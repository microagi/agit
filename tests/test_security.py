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
