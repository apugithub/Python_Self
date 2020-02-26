import pandas as pd

df = pd.read_csv('data/pokemon_data.csv') #Dataframe (the core of pandas)

#print(df)  # Print the dataframe
#print(df.info()) #Prints the summary of dataframe

#print(df.head()) # head prints first 5 records  + you may specify number inside head too

#print(df['HP'].max())  # displaying the max value of the column HP

#print(df.columns) # prints the column names

#print (df[['HP','Name']]) #Multiple columns... by specifying a list

#print(df['HP'][10:15])

#print(df.iloc[0:4,[0,1,2,3]])  # 0:4 is the index range of rows and [0,1,2,3] are the position of columns like 1st, 2nd

#print(df.loc[df['HP']==80])   #like where condition

#print(df.describe())

#print(df.shape) # returns number of rows and columns

print (df.count()) # returns column wise not null count


