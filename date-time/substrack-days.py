
import  datetime
today = datetime.date.today()
future = today+datetime.timedelta()
past = today-datetime.timedelta()
print("7 days:",future)
print("7 days:",past)
print(today)

