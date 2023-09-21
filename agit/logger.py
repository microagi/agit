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
