#!/usr/bin/python3
import sys
lazy_pagination = __import__('2-lazy_paginate').lazy_pagination

try:
    for page in lazy_pagination(100):
        for user in page:
            print(user)

except BrokenPipeError:
    sys.stderr.close()
