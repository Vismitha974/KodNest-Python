#  module  -- python file  reuseable

# def add(x,y):
#     return x + y
# def sub(x,y):
#     return x - y
# def mul(x,y):
#     return x * y
# def div(x,y):
#     if y == 0:
#         return "Cannot divide by zero"
#     return x / y

# package -- folder containing modules

# user-defined module
import calculatormodule as cm 

print(cm.add(10, 20))
print(cm.sub(10, 20))
print(cm.mul(10, 20))
print(cm.div(10, 20))

# built-in/ standard library (module --math, random)

from math import sqrt
from math import *
import math 
print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.factorial(5))

import random
print(random.randint(1, 10))