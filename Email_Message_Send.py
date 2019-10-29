import datetime
import smtplib
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class MessageUser():
    user_details = []
    email_messages = []
    base_message = """Hi {name}! 

        Thank you for the purchase on {date}. 
        Just as a reminder the purchase total was ${total}.
        Have a great one!

        Team SG
        """

    def add_user(self, name, amount, Email= None):
        name = name[0].upper() + name[1:].lower()  #Same as Initcap
        amount = "%.2f" % (amount) #Making the amount value to be 2 decimal
        detail = {
            "name" : name,
            "amount" : amount,
        }
        a = datetime.date.today()
        date_text = '{today1.day}/{today1.month}/{today1.year}'.format(today1=a)
        detail["date"] = date_text
        if Email is not None:     #This is same as if Email!= None
            detail["Email"] = Email
        self.user_details.append(detail)


    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) >0:
            for detail in self.get_details():
                name= detail["name"]
                amount = detail ["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name= name,
                    date = date,
                    total = amount
                )
                self.email_messages.append(new_msg)
            return self.email_messages
        return []

    def send_email(self):
        self.make_messages()
        if len(self.email_messages)>0 :
            for detail in self.email_messages:
                user_email = detail["Email"]
                user_message = detail[""]




obj = MessageUser()
obj.add_user("San", 123.65, "9176833080apu@gmail.com")
obj.add_user("jacob", 345.67, "9176833080apu@gmail.com")
obj.add_user("dAnial", 564, "9176833080apu@gmail.com")

obj.get_details()

print(obj.make_messages(), "\n")




