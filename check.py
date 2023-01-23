from todoist_api_python.api import TodoistAPI
import json
import pandas as pd
import requests
import logging
import time
from tqdm import tqdm
import sqlite3

start = time.time()

# #################### SQLite Config ###########################
db_location = 'D:/Essentials/Blue Bird ==========/Documents/Todoist/todoist.db'
db_connection = sqlite3.connect(db_location)
cursor = db_connection.cursor()
# #############################################################


# This logging configuration is to print the info on console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# ######################  Initial setup ########################################
f = open('D:/Essentials/Blue Bird ==========/Documents/Todoist/API_Keys.json')
keys = json.load(f)

headers = {
    "Authorization": 'Bearer {}'.format(keys['TODOIST_API'])
}
api = TodoistAPI(keys['TODOIST_API'])
logging.info('Initial setup done \n')
#####################################################################################
prio = {4: 1, 3: 2, 2: 3, 1: 4}

active_tasks_dict = {'Task_Name': [], 'Creation_Date': [], 'Due_Date': [], 'Priority': [],
                     'Task_ID': [], 'Project_ID': []}

project_ids = []
sync_param = {"sync_token": '*', "resource_types": '["all"]'}
sync = requests.post(url='https://api.todoist.com/sync/v9/sync', headers=headers,
                     params=sync_param)

# Below response will fetch all completed tasks (including deleted), and we need to pass only header for that
response_all_tasks = requests.post(url='https://api.todoist.com/sync/v9/completed/get_all', headers=headers)
c5 = response_all_tasks.json()
[project_ids.append(c5['items'][i]['project_id']) for i in range(len(c5['items']))]
project_ids = list(set(project_ids))


c = 0  # Just a counter
for j in project_ids:
    # The below response is to get the project-wise tasks(completed & is_deleted=false)
    response_task2 = requests.post(url='https://api.todoist.com/sync/v9/archive/items?project_id={}'.format(j),
                                   headers=headers, params={"limit": 1})  # Max limit 100
    c2 = response_task2.json()
    print(c2['total'])
    ab = api.get_project(project_id=j).name
    print(ab)

    '''if c2['total'] == 0:
        # Below part is to get the items's details
        for i in range(len(c2['items'])):
            # Below response is to fetch specific task (non deleted) details and we need to pass task id as param
            response_task = requests.post(url='https://api.todoist.com/sync/v9/items/get',
                                          headers=headers, params={"item_id": "{}".format(c2['items'][i]['id'])})
            task_json = response_task.json()
            # print(task_json)
            print('Task deleted: ', task_json['item']['content'], '  Completed on: ', task_json['item']['completed_at'])

    else:
        print('All clean !!  no completed items are pending to be deleted')

db_connection.close()
print('\n')
print('Total items deleted: ', c)
logging.info('Deleted items loaded in DB')'''



