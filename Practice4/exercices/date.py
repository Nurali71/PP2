# Write a Python program to subtract five days from current date.
import datetime
today=datetime.datetime.now()
print(today)
fiveday=datetime.timedelta(days=5)
result=today-fiveday
print(result)
# Write a Python program to print yesterday, today, tomorrow.

import datetime
today=datetime.datetime.now()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print(yesterday)
print(tomorrow)
# Write a Python program to drop microseconds from datetime.
import datetime
today=datetime.datetime.now()
print(today.strftime("%Y-%m-%d %H:%m:%S"))

# Write a Python program to calculate two date difference in seconds.
import datetime
date_str1 = input("Первая дата: ")
date_str2 = input()
date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

delta = date2 - date1
seconds = abs(delta.total_seconds())

print(f"{seconds}")