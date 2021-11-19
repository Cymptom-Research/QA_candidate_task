#!/usr/bin/env python3
#    ___                      _
#   / __\   _ _ __ ___  _ __ | |_ ___  _ __ ___
#  / / | | | | '_ ` _ \| '_ \| __/ _ \| '_ ` _ \
# / /__| |_| | | | | | | |_) | || (_) | | | | | |
# \____/\__, |_| |_| |_| .__/ \__\___/|_| |_| |_|
#       |___/          |_|
#
#
# Author: Ziv Kaspersky <ziv@cymptom.com> on 19/11/2021
from calc import Calculator


def test_add():
    # test basic functionality
    assert Calculator.add(4, 5) == 9

    # test addition with negative numbers
    assert Calculator.add(4, -5) == -1
    assert Calculator.add(-4, 5) == 1
    assert Calculator.add(-56, -47) == -101

    # ?
    assert Calculator.add(0, 0) == 0
    # ?
    assert Calculator.add(2 ** 36, 1) == 2 ** 36 + 1
