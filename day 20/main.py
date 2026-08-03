# 1. Built-in modules
import math

print(math.sqrt(16))      # square root
print(math.pi)            # pi value
print(math.factorial(5))  # factorial

import random

print(random.randint(1, 10))     # random number between 1-10
print(random.choice(["a", "b", "c"]))  # random item from a list

import datetime

print(datetime.datetime.now())   # current date & time

# 2. Importing only specific functions
from math import sqrt, pi

print(sqrt(25))   # no need to write "math." anymore
print(pi)

#3. Importing with an alias
import math as m

print(m.sqrt(9))
# 4. this imports from calculator.py
import calculator

print(calculator.add(5, 3))
print(calculator.subtract(10, 4))