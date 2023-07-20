# Copyright (C) 2023 Sivan Grünberg <sivan@vitakka.co>
# Vitakka Consulting https://vitakka.co
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
from agit.config import DESTRUCTIVE_COMMANDS


def is_destructive(command):
    for destructive_command, why in DESTRUCTIVE_COMMANDS.items():
        if destructive_command in command:
            return (True, why)
    return (False, "non destructive.")
