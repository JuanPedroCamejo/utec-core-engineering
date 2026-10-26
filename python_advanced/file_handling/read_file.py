#!/usr/bin/env python3
"""Module for reading and printing the contents of a UTF-8 text file."""


def read_file(filename=""):
    """Read a text file in UTF-8 and print its contents to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
