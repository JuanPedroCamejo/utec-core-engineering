#!/usr/bin/env python3
for first in range(10):
    for second in range(first + 1, 10):
        separator = ", " if first < 8 or second < 9 else "\n"
        print("{:d}{:d}".format(first, second), end=separator)
