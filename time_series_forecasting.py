import pandas as pd
import calendar
from calendar import monthrange
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


# Below dict month wise index value
month_dict = {month: index for index, month in enumerate(calendar.month_abbr) if month}  # Ex- {'Jan': 1}

db_location = 'D:/Pictures/'

df = pd.read_excel(db_location + 'Monthly Expenditure.xlsx', sheet_name='Sheet1').fillna(0)
cols = (df.columns[1:])  # Collection columns starting Jul-13 expect the first column (Date)

daily_expense = []  # To capture the expense values
dates = []  # To capture the dates

# Collecting month wise expense data (traversing only required days of month e.g Jan 31 days, Nov 30 days)
# monthrange will give tuple of 1st day and count of the month e.g monthrange(2011, 2) => (1, 28)
for i in cols:
    try:
        [daily_expense.append(j) for j in df[i][0:monthrange(int('20' + i[-2:]), month_dict.get(i[:3]))[1]].tolist()]
    except Exception as e:
        print(e)
    # print(i, ' == ', monthrange(int('20' + i[-2:]), month_dict.get(i[:3])))
print(len(daily_expense))


# Below line is to get date range similar to the length of expenses data
date_range = pd.date_range('2013-07-01', periods=len(daily_expense), freq='D')  # D for daily


# Converting dates to YYYY-MM-DD format
for z in range(len(daily_expense)):
    dates.append(date_range[z].strftime('%Y-%m-%d'))
print(len(dates))

# Creating dataframe with dates and expenses
df_final = pd.DataFrame(zip(dates, daily_expense), columns=['Date', 'Daily_Expense'])
# df_final.to_csv(db_location+'Temp_out.csv')
# df_final.to_excel(db_location+'Temp_out.xlsx', index=False)
# print(df_final.where(df_final['Date'] == '2023-05-05').dropna())


df_final.set_index('Date', inplace=True)
print(df_final.head(30))
df_final.plot()
# plt.show()

#
# def window_input_output(input_length: int, output_length: int, data: pd.DataFrame) -> pd.DataFrame:
#     df1 = data.copy()
#
#     i1 = 1
#     while i1 < input_length:
#         df1[f'x_{i1}'] = df1['Daily_Expense'].shift(-i1)
#         i1 = i1 + 1
#
#     j = 0
#     while j < output_length:
#         df1[f'y_{j}'] = df1['Daily_Expense'].shift(-output_length - j)
#         j = j + 1
#
#     df1 = df1.dropna(axis=0)
#
#     return df1
#
#
# seq_df = window_input_output(200, 200, df_final)
# print(seq_df)
#
#
# X_cols = [col for col in seq_df.columns if col.startswith('x')]
#
# X_cols.insert(0, 'co2')
#
# y_cols = [col for col in seq_df.columns if col.startswith('y')]
# X_train = seq_df[X_cols][:-2].values
# y_train = seq_df[y_cols][:-2].values
#
# X_test = seq_df[X_cols][-2:].values
# y_test = seq_df[y_cols][-2:].values
