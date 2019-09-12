# In this program make message is formed in a different way

import datetime

class MessageUser():
    user_details = []
    message =[]
    default_msg = """Hi {name}!
                  Thank you for the purchase on {date}. 
                  Just as a reminder the purchase total was ${total}.
                  Have a great one! """

    def add_user(self, name, amount, email = None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail= {
            "name": name,
            "amount" : amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail ['date'] = date_text
        if email is not None:
            detail['email']=email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_message (self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                date = detail["date"]
                total = detail["amount"]
                message = self.default_msg
                new_msg= message.format(
                    name = name,
                    date = date,
                    total = total
                )
                self.message.append(new_msg)
            return (self.message)
        return []

obj = MessageUser()
obj.add_user("Santanu", 123.67)
obj.add_user("David", 321, "devid@aolmail.com")
obj.add_user("Danny", 654)
print(obj.make_message())
obj.get_details()



