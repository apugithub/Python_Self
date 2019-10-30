import datetime
import smtplib
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = '9176833080apu@gmail.com'
password = '9176833080'
from_email = username

class MessageUser():
    user_details = []
    messages = []
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
        print(detail)


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
                user_email= detail.get("Email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []

    def send_email(self):
        self.make_messages()
        if len(self.email_messages)>0 :
            for detail in self.email_messages:
                user_email = detail["email"]
                user_message = detail["message"]
                try:
                    email_conn= smtplib.SMTP('smtp.gmail.com:587')
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    the_msg = MIMEMultipart()
                    the_msg["Subject"] = "Billing Invoice"
                    the_msg["From"] = from_email
                    the_msg["To"] = user_email
                    part_1 = MIMEText(user_message, 'plain')
                    the_msg.attach(part_1)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                    print("Email sent successfully to: " + user_email)
                except smtplib.SMTPException:
                    print("error sending message")
            return True
        return False




obj = MessageUser()
obj.add_user("jacob", 345.67,  "9176833080apu@gmail.com")
obj.add_user("dAnial", 564,  "9176833080apu@gmail.com")

#obj.get_details()

obj.send_email()






