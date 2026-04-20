# EXCEPTION
# try:
#     x = int("abc")
# except Exception as e:
#     print("error:",e)

# StopIteration

# nums = [1,2,3,4]
# it = iter(nums)
# print(next(it))
# print(next(it))


# ArithmeticError

try:
    x = 10 / 0
except ArithmeticError:
    print("Arithmatic error")


# OverflowError

import math

try:
    print(math.exp(710))
except OverflowError:
    print("number is smallest")