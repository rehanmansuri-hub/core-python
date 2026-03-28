
import datetime

dob = datetime.date(2006, 11, 17)
today = datetime.date.today()

age = today.year - dob.year

day_name = dob.strftime("%A")

print("Your age is:", age)
print("You were born on:", day_name)
