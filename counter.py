#!/usr/bin/env python3
#    ___                      _
#   / __\   _ _ __ ___  _ __ | |_ ___  _ __ ___
#  / / | | | | '_ ` _ \| '_ \| __/ _ \| '_ ` _ \
# / /__| |_| | | | | | | |_) | || (_) | | | | | |
# \____/\__, |_| |_| |_| .__/ \__\___/|_| |_| |_|
#       |___/          |_|
#
# CYMPTOM LABS Copyright 2020. All rights reserved.
#
# Author: Ziv Kaspersky <ziv@cymptom.com> on 19/11/2021
from typing import List


def counter(items):
    """
    Does some magical things!
    :param items: A list of objects
    :return: what do you think?
    """
    items_counter = {}
    for item in set(items):
        items_counter[item] = items.count(item)
    return items_counter
