#!/usr/bin/env python3
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in 'qe':
        pass
print(''.join(chr(letter) for letter in range(ord('a'), ord('z') + 1) if chr(letter) not in 'qe'))
