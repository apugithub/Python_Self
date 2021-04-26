import pandas as pd

df = pd.read_csv("E:/hadoop/test.csv").fillna("NA")

# With as_index = False grouped by records will appear in every row
df1 = df.groupby(['country','service'], as_index=False).agg(set) #.values.tolist()

# Records wise oriented
df2 = df1.to_dict(orient='records')