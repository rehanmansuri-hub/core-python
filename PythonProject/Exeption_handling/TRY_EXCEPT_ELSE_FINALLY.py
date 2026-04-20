try:
    num = 20
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid exception")
else:
    print("Result is:", result)
finally:
    print("This block always executes.")