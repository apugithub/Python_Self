# This programe will act like a mail merge, where the message body is same but the 'name' , 'amount' and 'product' varies
import datetime

default_names = ["Steven", "San", "david","ann", "Nicole", "brad"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323]
default_products = ["Pen", "Book", "Bottle", "Phone", "Fruits", "Software"]

default_msg = """Hi {name}! 
              Thanks for purchasing the {product} on {date}
              Your total amount is Rs {amount}"""

def make_message (names, products, amounts):
    if len(default_names) == len(default_amounts) or len(default_names)== len(default_products):
        i = 0
        today1 = datetime.date.today()
        text = '{today.day}/{today.month}/{today.year}'.format(today=today1)
        for j in names:
            j = j.capitalize()  # This is to capitalize the names if in lower case.
            new_product = products[i]
            new_amount = "%.2f" % amounts[i]
            new_message = default_msg.format(
                name=j,
                product=new_product,
                date=text,
                amount=new_amount
            )
            i = i+1
            print (new_message, "\n")


make_message(default_names, default_products, default_amounts)






