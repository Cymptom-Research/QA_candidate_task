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

class Calculator:
    """Very simple calculator"""

    @staticmethod
    def add(x, y):
        """This function adds two numbers"""
        return x + y

    @staticmethod
    def subtract(x, y):
        """This function subtracts two numbers"""
        return x - y

    @staticmethod
    def multiply(x, y):
        """This function multiplies two numbers"""
        return x * y

    @staticmethod
    def divide(x, y):
        """This function divides two numbers"""
        return x / y
