import pandas as pd
import json
import os
file = 'C:\\Users\\Blue Bird\\Desktop\\test.xlsx'
f = open('C:\\Users\\Blue Bird\\Desktop\\test.json', 'w')

excel_data = pd.read_excel(file, sheet_name=['Sheet1'], na_values='NaN')
excel_to_df = excel_data['Sheet1'].fillna(0)  # After this step ['Sheet1'] only 'excel_to_df' becomes data frame
all = excel_to_df.to_json(indent=4, orient='records') # This will give date wise summary JSON
#f.close()
print(all)


final=excel_to_df.to_dict()
month_json = json.dumps(final, indent=4)  # This JSON will show month-wise details
# print(month_json)




