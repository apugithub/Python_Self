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


active_tasks_dict = {'Task_Name': [], 'Creation_Date': [], 'Due_Date': [], 'Priority': [],
                     'Task_ID': [], 'Project_ID': []}

prio_dict = {4: 1, 3: 2, 2: 3, 1: 4}

project_ids = []  # Project having tasks
sync_param = {"sync_token": '*', "resource_types": '["all"]'}
sync = requests.post(url='https://api.todoist.com/sync/v9/sync', headers=headers,
                     params=sync_param)
logging.info('Syncing is done')


# Getting ACTIVE tasks & loading into JSON & Taking DB Backup
logging.info('Getting Active tasks..\n')
active_tasks = api.get_tasks()
try:
    for i in tqdm(range(len(active_tasks))):  # tqdm along with time.sleep is for progress bar only
        active_tasks_dict['Task_Name'].append(active_tasks[i].content)
        active_tasks_dict['Creation_Date'].append(active_tasks[i].created_at)
        active_tasks_dict['Due_Date'].append(active_tasks[i].due.to_dict().get('date'))
        active_tasks_dict['Task_ID'].append(active_tasks[i].id)
        active_tasks_dict['Project_ID'].append(active_tasks[i].project_id)
        prio = 4 if active_tasks[i].priority == 1 else (
            3 if active_tasks[i].priority == 2 else (2 if active_tasks[i].priority == 3 else 1))
        active_tasks_dict['Priority'].append(prio)
        # Priority is stored reverse eg. frontend Priority 1 = backend Priority 4,
        # frontend Priority 2 = backend Priority 3
        time.sleep(0.01)

    df = pd.DataFrame(active_tasks_dict).sort_values(by=['Due_Date', 'Priority'], ascending=True)
    df.to_json(r'D:/Essentials/Blue Bird ==========/Documents/Todoist/Todoist_99.json', orient='records', indent=4)
    logging.info('JSON Backup taken successfully\n')

except Exception as error:
    print(error)


# ###############  Inserting Active tasks in SQLite DB  ############################################
logging.info('Loading Active tasks into DB....(truncate & load)\n')

try:
    cursor.execute('DELETE FROM todoist')  # This is truncate and load process

    for i in tqdm(range(len(active_tasks_dict['Task_Name']))):

        insert_query = '''INSERT INTO todoist (name, duedate, priority, created_at) 
                          VALUES ("{0}", '{1}', {2}, '{3}')''' \
            .format(active_tasks_dict['Task_Name'][i], active_tasks_dict['Due_Date'][i],
                    active_tasks_dict['Priority'][i], active_tasks_dict['Creation_Date'][i])

        cursor.execute(insert_query)
        db_connection.commit()
        time.sleep(0.001)

    count = cursor.execute('select count(*) from todoist')
    print('Records inserted successfully in SQLite DB: ', count.fetchone()[0])
    # fetchone() [0]  gives the rowcount


except sqlite3.Error as e:
    logging.info('Failed to insert due to error : ', e)


# ########################### Operations on deleted items ###########################

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

    # Below part is to get the items's details
    for i in range(len(c2['items'])):
        # Below response is to fetch specific task (non deleted) details and we need to pass task id as param
        response_task = requests.post(url='https://api.todoist.com/sync/v9/items/get',
                                      headers=headers, params={"item_id": "{}".format(c2['items'][i]['id'])})
        task_json = response_task.json()
        # print(task_json)
        print('Task deleted: ', task_json['item']['content'], '  Completed on: ', task_json['item']['completed_at'])

        insert_archive = '''insert into todoist_archive (name, duedate, priority, date_added, date_completed) \
                    values (?,?,?,?,?)'''
        try:
            cursor.execute(insert_archive, (task_json['item']['content'], task_json['item']['due']['date'],
                                            prio_dict.get(task_json['item']['priority']), task_json['item']['added_at'],
                                            task_json['item']['completed_at']))
            db_connection.commit()
            c = c + 1
        except sqlite3.Error as s:
            print('There are issues during SQLite archival: ', s)

        # Deleting the task
        api.delete_task(task_id=c2['items'][i]['id'])

print('\n')
print('Total items deleted: ', c)
logging.info('Deleted items loaded in DB')

db_connection.close()
print('\nOperation complete !! Total time taken {} seconds\n\n'.format(round(time.time()-start), 2))








