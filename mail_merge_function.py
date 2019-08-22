import datetime

default_names = ["Steven", "San", "David","Ann", "Nicole", "Brad"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323]
default_products = ["Pen", "Book", "Bottle", "Phone", "Fruits", "Software"]

default_msg = """Hi {name}! 
              Thanks for purchasing the {product} on {date}
              Your total amount is Rs {amount}"""

def make_message (names, products, amounts):
    if len(default_names) == len(default_amounts) or len(default_names)== len(default_products):
        i = 0
        today1 = datetime.date.today()
        text = "{today.day}/{today.month}/{today.year}".format(today=today1)
        for name in names:
            new_amount = "%.2f" %(amounts[i])
            new_product = products[i]
            new_msg = default_msg.format(
                name = j
                product = new_product
                date = text
                amount = new_amount
            )




