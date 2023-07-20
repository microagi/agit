# Copyright (C) 2023 Sivan Grünberg <sivan@vitakka.co>
# Vitakka Consulting https://vitakka.co
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
import logging
import sys


def get_logger(level=logging.INFO):
    # Create a file handler
    handler = logging.StreamHandler(sys.stdout)

    # Create a formatter and set it to the handler
    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
    handler.setFormatter(formatter)

    log = logging.getLogger(__name__)

    # Add the handler to the logger
    log.addHandler(handler)

    log.setLevel(level=level)
    return log


mylogger = get_logger()
