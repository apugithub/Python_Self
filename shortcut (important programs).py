import tkinter as tk

root = tk.Tk()
root.title ("Important Programs")

canvas1 = tk.Canvas(root, width=700, height=300)
canvas1.pack()

# Now the below definitions are pointing to the python files...so when you are calling these functions, its in turn
# runs the associated python file.

def test ():
    import AM_PM

def covid_email ():
    import covid_data_email

def nav_extraction ():
    import nav_extraction

def png_to_jpg ():
    import PNG_to_JPG_Converter

def send_email_fund_nav():
    import send_email_fund_NAV

button1 = tk.Button(root, text=' Exit Application ', command=root.destroy, bg='white', fg='black')
canvas1.create_window(300, 270, window=button1)

button2 = tk.Button(root, text=' Covid Stat (Email) ', command=covid_email, bg='palegreen2', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(80, 50, window=button2)

button3 = tk.Button(root, text=' NAV Extraction ', command=nav_extraction, bg='yellow', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(250, 50, window=button3)

button4 = tk.Button(root, text=' PNG to Jpeg ', command=png_to_jpg, bg='violet', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 50, window=button4)

button5 = tk.Button(root, text=' AM_PM (Test) ', command=test, bg='orange', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(550, 50, window=button5)

button6 = tk.Button(root, text=' Send Email (Fund NAV) ', command=send_email_fund_nav, bg='blue', fg='white', font=('Arial', 11, 'bold'))
canvas1.create_window(95, 100, window=button6)

root.mainloop()