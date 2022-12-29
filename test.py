from todoist.api import TodoistAPI
import pandas as pd
import json
import time
from tqdm import tqdm
import sqlite3


start = time.time()

db_location = 'D:/Essentials/Blue Bird ==========/Documents/Todoist/todoist.db'
db_connection = sqlite3.connect(db_location)
cursor = db_connection.cursor()
# #############################################################

f = open('D:/Essentials/Blue Bird ==========/Documents/Todoist/API_Keys.json')
keys = json.load(f)

api = TodoistAPI(keys['TODOIST_API'])

completed_task_list = []

completed_tasks = api.items.get_completed(project_id=2161862569)  # a maximum of 100 tasks is supported per batch
for j in completed_tasks:
    completed_task_list.append(j['id'])

print(completed_task_list)

# print((api.items.all()[0]['due'].get('date')))
# for i in range(len(api.items.all())):
    # print((api.items.all()[i]['id']))

# item_list = [6411360489, 5387778650]

for ii in completed_task_list:
    for jj in range(len(api.items.all())):
        if ii == api.items.all()[jj]['id']:
            item = api.items.all()[jj]
            print(item)
            print('Item Deleted: ' + item['content'])
            prt = 4 if item['priority'] == 1 else (3 if item['priority'] == 2 else (2 if item['priority'] == 3 else 1))
            print(item['content'], item['due']['date'], prt, item['date_added'], item['date_completed'])

projects = api.state['projects']

print((api.items.all()))
