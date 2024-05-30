#!/usr/bin/env python3

# Author: [Your Full Name]
# Author ID: [Your Seneca ID]
# Date Created: [yyyy/mm/dd]

import sys

# Default timer value
timer = 3

# Check if an argument was provided
if len(sys.argv) > 1:
    # Use the argument as the timer value
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

