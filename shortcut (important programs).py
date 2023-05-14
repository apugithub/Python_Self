import tkinter as tk

root = tk.Tk()
root.title("Important Programs")

canvas1 = tk.Canvas(root, width=700, height=300)
canvas1.pack()

# Now the below definitions are pointing to the python files...so when you are calling these functions, its in turn
# runs the associated python file.

def test ():
    import AM_PM

def covid_email ():
    import covid_data_email

def nav_extraction ():
    import nav_extraction_rapidapi

def png_to_jpg ():
    import PNG_to_JPG_Converter

def send_email_fund_nav():
    import send_email_fund_NAV

def todo_ist():
    import todo_ist

def google_task_sync():
    import google_task_sync_todoist

def balance_mf_bank():
    import balance_to_maintain

def age_cal():
    import age_calc

def remove_pdf_pass ():
    import remove_pdf_password

def flask2_run():
    import flask2_run


button1 = tk.Button(root, text=' Exit Application ', command=root.destroy, bg='white', fg='black')
canvas1.create_window(300, 270, window=button1)

button2 = tk.Button(root, text=' Age Calculation ', command=age_cal, bg='palegreen2', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(80, 50, window=button2)

button3 = tk.Button(root, text=' NAV Extraction ', command=nav_extraction, bg='yellow', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(250, 50, window=button3)

button4 = tk.Button(root, text=' PNG to Jpeg ', command=png_to_jpg, bg='violet', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 50, window=button4)

button5 = tk.Button(root, text=' Remove PDF Pass ', command=remove_pdf_pass, bg='orange', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(550, 50, window=button5)

button6 = tk.Button(root, text=' Send Email (Fund NAV) ', command=send_email_fund_nav, bg='blue', fg='white', font=('Arial', 11, 'bold'))
canvas1.create_window(95, 100, window=button6)

button7 = tk.Button(root, text=' ToDoist Sync ', command=todo_ist, bg='orange', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(270, 100, window=button7)

button8 = tk.Button(root, text=' GoogleTask Sync ', command=google_task_sync, bg='palegreen2', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(420, 100, window=button8)

button9 = tk.Button(root, text=' MF Balance Maintain ', command=balance_mf_bank, bg='red', fg='black', font=('Arial', 11, 'bold'))
canvas1.create_window(600, 100, window=button9)

button10 = tk.Button(root, text=' Flask2 Run ', command=flask2_run, bg='indigo', fg='white', font=('Arial', 11, 'bold'))
canvas1.create_window(60, 150, window=button10)

root.mainloop()
