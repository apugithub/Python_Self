import sqlite3
import json
from tqdm import tqdm
import time

start = time.time()

db_location = 'D:/Essentials/Blue Bird ==========/Documents/Todoist/todoist.db'


print('\nSQLite records insertion started ')


db_connection = sqlite3.connect(db_location)
cursor = db_connection.cursor()
print('Connected to SQLite DB\n')


count = cursor.execute('select * from todoist')
#cursor.execute('select count(name) as ct, duedate from todoist group by duedate having count(name)> 2 order by ct desc')
c = count.fetchall()  # fetchone() [0]  gives the rowcount
db_connection.close()

print(len(c))


