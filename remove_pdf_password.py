#  Last updated on 20th June 2023

import pikepdf as pp
import json
import os
import calendar
from datetime import datetime

# Calculation of current month , prev month and year
current_year = datetime.now().year
curr_month_index = datetime.now().month
current_month = calendar.month_name[curr_month_index]
previous_month = calendar.month_name[curr_month_index - 1]


f = open('D:/Essentials/Blue Bird ==========/Documents/Todoist/API_Keys.json')
keys = json.load(f)
output_dir = 'C:\\Users\\Blue Bird\\Desktop\\Password_Removed_PDFs\\'
current_organization = 'ANZ '
orig_file = 'payslip'
file_name = None  # 'Income Tax Worksheet FY-2022-23'
pass_1 = keys['Date_pass']  # DDMMYYYY
generic_file = None
generic_file_pass = None


# Get the file if its ANZ or any other pdf file
print('Is it for ANZ pdf?')
b = input()

if b.upper() == 'Y':
    # Getting User Input and framing the file name
    print('Enter value Y if its for current month else N\n')
    a = input()

    if a.upper() == 'Y':
        file_name = current_organization + current_month + ' ' + str(current_year) + ' Payslip'
    else:
        file_name = current_organization + previous_month + ' ' + str(current_year) + ' Payslip'
else:
    print('Enter the non-ANZ pdf file name, you want to remove password from ')
    generic_file = input()
    print('\nEnter the password for the file')
    generic_file_pass = input()


# Main process to remove pass and save the file
try:
    # Check if the output folder exists, else create a new one
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    pdf = pp.open('C:\\Users\\Blue Bird\\Desktop\\{}.pdf'.format(orig_file if b.upper() == 'Y' else generic_file),
                  password=pass_1 if b.upper() == 'Y' else generic_file_pass)
    # pdf.save('D:/Essentials/Blue Bird ==========/{}.PDF'.format(file_name))
    pdf.save(output_dir + '{}.PDF'.format(file_name if b.upper() == 'Y' else generic_file))
    print('==== Ignore previous parsing error')
    print('Pass is removed successfully !!')
    print('Operation complete !!!')
except Exception as e:
    print(e)
