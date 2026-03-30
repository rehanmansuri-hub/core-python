import datetime


today = datetime.date.today()

future = today  + datetime.timedelta(days=2)
past = today - datetime.timedelta(days=2)

print("2 days:",future)
print("2 days:",past)

print(today)

