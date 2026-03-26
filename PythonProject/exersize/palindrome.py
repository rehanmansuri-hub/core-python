number = 404
n = number
sum = 0
rem = 0
while n > 0:
     rem = n / 10
     sum = sum*10+rem
     n = n //10
if sum == number:
     print("palindrome number",number)
else:
     print("not palindrome number",number)

number = 121
n = number
sum = 0
rem = 0
while n > 0:
    rem = n / 10
    sum = sum*10+rem
    n = n//10
if sum == number:
    print("palindrome number",number)
else:
    print("not palindrome",number)
