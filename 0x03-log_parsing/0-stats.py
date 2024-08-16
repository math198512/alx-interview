#!/usr/bin/python3
"""Log parsing using pyhton"""
import random
import sys
from time import sleep
import datetime
import signal


def logger():
    """script that reads stdin line by line and computes metrics"""
    count = 0
    total_file_size = 0
    for line in sys.stdin:
        count += 1
        x = line.split()
        total_file_size += int(x[-1])
        if count == 10:
            print("File size:", total_file_size)
            count = 0


logger()
