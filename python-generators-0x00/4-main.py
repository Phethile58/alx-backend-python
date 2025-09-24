#!/usr/bin/python3
from itertools import islice
ages = __import__('3-average_age').stream_user_ages

# Print only the first 5 user ages
for age in islice(ages(), 5):
    print(age)
