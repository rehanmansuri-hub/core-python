# list = [100, 10, 11, 5, 13, 17, 88]
#
# for i in range(len(list)):
#      if list[i] == 100:
#          a = list[i]
#          for j in range(i+1, len(list)):
#              if list[j] < a:
#                  b = list[j]
# print("a =", a)
# print("b =", b)


list = [100, 10, 11, 5, 13, 17, 88]

for i in range(0, len(list)):
    for j in range(i + 1, len(list)):
        if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    print(list[i], end=" ")
