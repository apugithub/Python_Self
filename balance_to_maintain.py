# This code will give you the balance to be maintained in banks for MF on a given date for the rest of the month

from datetime import date, datetime

current_date = date.today()  # 2022-09-03
current_month = datetime.now().strftime("%B")
current_year = datetime.now().strftime("%y")
# print(current_year)
print('\nToday\'s date: ', current_date)
current_date_str = int(current_date.strftime("%d"))
# current_date_str = 21
# print(current_date, 'and', current_date_str)


# Axis ASAP (MF)
df_axis = {4: 4989, 7: 4000, 18: 5248, 19: 4988}
# SBI_2 (MF)
df_sbi2 = {3: 4086, 15: 6711, 21: 2500, 28: 7872}


def calculate(df):
    df_keys = list(df.keys())
    df_keys.sort(reverse=False)  # This is to make sure in list dates are ordered in asc order
    amount = 0
    for i in df_keys:
        if i >= current_date_str:
            amount = amount + (df[i])
    return amount


print('Balance to maintain (Axis ASAP) for MF as of today for the current month {}: Rs'.format(current_month+'\''+current_year), calculate(df_axis), '\n')
print('======================================================\n')
print('Balance to maintain (SBI_2) for MF as of today for the current month {}: Rs'.format(current_month+'\''+current_year), calculate(df_sbi2))
