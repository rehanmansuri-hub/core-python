number = [10, 20, 30, 50, 40, 60, 80, 70, 90, 25, 35, ]
# largest  = number[0]
# for num in number:
#     if num > largest:
#         largest = num
# print("largest number is",largest)
#
# number = [10, 20, 30, 50, 40, 60, 80, 70, 90, 25, 35]
#
# largest = max(number)
# number.remove(largest)
# second_largest = max(number)
#
# print(second_largest)

largest = max(number)
number.remove(largest)
second_largest = max(number)

print(second_largest)