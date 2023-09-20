#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ascii_c = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Convert ASCII values to characters and join them to form a string
flag = ''.join(chr(char) for char in ascii_c)

print("Here is your flag:")
print(flag)
