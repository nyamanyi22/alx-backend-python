#!/usr/bin/python3
import sys
stream_ages = __import__('4-stream_ages')

try:
    stream_ages.compute_average_age()
except BrokenPipeError:
    sys.stderr.close()
