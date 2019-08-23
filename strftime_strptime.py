import datetime

date1= datetime.datetime.today().strftime("%Y")
date2 = "20th June 1991"
#date_object = datetime.datetime.today()
date_object = datetime.datetime.strptime(date2, "%dth %B %Y") #strptime makes a string to date format
formatted_date = date_object.strftime("%d"+"-"+"%m"+"-"+"%Y") #strftime makes a date to required string format


print(date_object)
print(formatted_date)
print("Type of date_object= ", type(date_object))
print("Type of formatted_date= " , type(formatted_date))
