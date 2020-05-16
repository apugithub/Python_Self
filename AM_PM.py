import datetime


a = datetime.datetime.now()  # This prints 2020-05-07 23:08:56.574927
b = a.strftime("%d-%m-%Y, %I:%M:%S %p")  # This prints 07-05-2020, 11:08:56 PM    %p is for AM/PM
c = a.strftime("%d-%m-%Y, %H:%M:%S")  # This prints 07-05-2020, 23:10:31    %H for 24 hrs format

time_zone =  datetime.datetime.now().astimezone().tzname()   #Display local timezone name

print (a)
print(b)
print(c)
print(time_zone)