import pandas as pd

df = pd.read_csv('E:/hadoop/test.csv').fillna("NA")



df2 = df.groupby(['country','service'], as_index=False).agg(list)

#df2.to_csv('E:/hadoop/test_op.csv')
df3 = df2.to_dict(orient='records')

#print(df3)


a = [1,2,3,4,5]
print(set(a))