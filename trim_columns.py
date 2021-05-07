import pandas as pd

df = pd.read_csv ("E:/hadoop/test.csv")

def trim_all_columns(df):
    trim_strings = lambda x : x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)

df = trim_all_columns(df)

#df.to_csv("E:/hadoop/test_converted.csv", index= False, header= True)

print(df)