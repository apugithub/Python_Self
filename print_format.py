import datetime

datetime_object = datetime.date.today()
print(datetime_object)

quantity = 3
itemno = 567
price = 9;
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars on date {3}."
print(myorder.format(quantity, itemno, price, datetime_object))