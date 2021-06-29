import sqlite3
import json
from tqdm import tqdm
import time

start = time.time()

db_location = 'D:/Essentials/Blue Bird ==========/Documents/Todoist/todoist.db'
todoist_json = open('D:/Essentials/Blue Bird ==========/Documents/Todoist/Todoist.json', 'r')

print('\nToDoIst to SQLite records insertion started ')

todoist_data = json.load(todoist_json)
db_connection = sqlite3.connect(db_location)
cursor = db_connection.cursor()
print('Connected to SQLite DB\n')

try:
    cursor.execute('DELETE FROM todoist')

    for i in tqdm(todoist_data):

        insert_query = '''INSERT INTO todoist (name, duedate, priority) VALUES ("{0}", '{1}', {2})''' \
            .format(i['Task_Name'], i['Due_Date'], i['Priority'])

        cursor.execute(insert_query)
        db_connection.commit()
        time.sleep(0.001)

    count = cursor.execute('select count(*) from todoist')
    print('\nRecords inserted successfully in SQLite DB: ', count.fetchone()[0])  # fetchone() [0]  gives the rowcount


except sqlite3.Error as e:
    print('Failed to insert due to error : ', e)

finally:
    db_connection.close()
    print('\nOperation complete !! Total time taken {} seconds'.format(round(time.time() - start), 2))
