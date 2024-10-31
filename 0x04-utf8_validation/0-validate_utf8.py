#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""

    num_of_bytes = 0
    for num in data:
        if num_of_bytes > 0:
            if num >> 6 != 0b10:
                return False
            num_of_bytes -= 1
        else:
            if num >> 7 == 0:
                num_of_bytes = 0
            elif num >> 5 == 0b110:
                num_of_bytes = 1
            elif num >> 4 == 0b1110:
                num_of_bytes = 2
            elif num >> 3 == 0b11110:
                num_of_bytes = 3
            else:
                return False
    return num_of_bytes == 0
