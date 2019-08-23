# This program will auto increment the date till the range specified.

import datetime

date1 = datetime.datetime.today().date()  #with the use of date() you will get only the date part.
print("Today is : " , date1)

for i in range (1,4):
    date2 = datetime.datetime.today().date() + datetime.timedelta(days=i)
    #print("After ", i , " day/days : ", date2 )
    print("After %d day/days : " %i, date2) # Prev line and this line will print the same




