from todoist.api import TodoistAPI
import pandas as pd
import json
import time
from tqdm import tqdm
import sqlite3

start = time.time()

f = open('D:/Essentials/Blue Bird ==========/Documents/Todoist/API_Keys.json')
keys = json.load(f)

api = TodoistAPI(keys['TODOIST_API'])
api.sync()

projects = api.state['projects']
items = api.items.all()   # This contains Not completed & Completed tasks but not the deleted tasks

project_details = {'proj_name': [], 'proj_id': []}
projects_with_tasks = set()  # Set is used to retain only unique values
completed_task_list = []
active_tasks = {'Task_Name': [], 'Due_Date': [], 'Priority': [], 'Task_ID': [], 'Project_ID': []}

print('\n\nTotal Projects: ', len(projects))
print('Total Tasks [Completed + Non-Completed]: ', len(items))

for i in range(len(items)):
    projects_with_tasks.add(items[i]['project_id'])

print('Project IDs with tasks: ', list(projects_with_tasks))  # Here converted to list from set

for i in projects_with_tasks:
    completed_tasks = api.items.get_completed(project_id=i)  # a maximum of 100 tasks is supported per batch
    for j in completed_tasks:
        completed_task_list.append(j['id'])


# For deleting completed tasks


def delete_completed(item_list):
    if not item_list:  # To check if a list is empty
        print('\n' + 'No Completed Tasks Available for Delete')
        # print('Total active tasks: {}'.format(len(items)), end='\n\n')
    else:
        print('\n\n' + 'Number of tasks to be deleted: {}\n'.format(len(item_list)))
        c = 0
        for ii in item_list:
            item = api.items.get_by_id(ii)
            print('Item Deleted: ' + item['content'])
            item.delete()
            api.commit()
            c = c+1
        print('\nTasks Deleted: ', c)
        # print('Total Active Tasks after delete: ', len(items)-c, end='\n\n')


delete_completed(completed_task_list)


# Project Details dict formation (This includes all the projects even if it does not have a task)
for i in range(len(projects)):
    project_details['proj_name'].append(projects[i]['name'])
    project_details['proj_id'].append(projects[i]['id'])


# For Adding Project
def add_project(proj_name):
    api.projects.add(proj_name)
    api.commit()


items1 = api.items.all()  # Taking items after delete operation (of completed tasks)
print('\nTotal Active Tasks Currently: ', len(items1))

# Get Task Details
print('Backup Process Started...\n')
for i in tqdm(range(len(items1))):  # tqdm along with time.sleep is for progress bar only
    active_tasks['Task_Name'].append(items1[i]['content'])
    active_tasks['Due_Date'].append(items1[i]['due']['date'])
    active_tasks['Task_ID'].append(items1[i]['id'])
    active_tasks['Project_ID'].append(items1[i]['project_id'])
    prio = 4 if items1[i]['priority'] == 1 else (
        3 if items1[i]['priority'] == 2 else (2 if items1[i]['priority'] == 3 else 1))
    active_tasks['Priority'].append(prio)
    # active_tasks['Priority'].append(items1[i]['priority'])
    # Priority is stored reverse eg. frontend Priority 1 = backend Priority 4, frontend Priority 2 = backend Priority 3
    time.sleep(0.01)

df = pd.DataFrame(active_tasks).sort_values(by=['Due_Date', 'Priority'], ascending=True)
df.to_json(r'D:/Essentials/Blue Bird ==========/Documents/Todoist/Todoist.json', orient='records', indent=4)

print('\n' + 'JSON Backup taken successfully')


# ###############  Inserting records in SQLite DB  ############################################
print('\nSQLite records insertion started ')

db_location = 'D:/Essentials/Blue Bird ==========/Documents/Todoist/todoist.db'

db_connection = sqlite3.connect(db_location)
cursor = db_connection.cursor()
print('Connected to SQLite DB\n')

try:
    cursor.execute('DELETE FROM todoist')

    for i in tqdm(range(len(active_tasks['Task_Name']))):

        insert_query = '''INSERT INTO todoist (name, duedate, priority) VALUES ("{0}", '{1}', {2})''' \
            .format(active_tasks['Task_Name'][i], active_tasks['Due_Date'][i], active_tasks['Priority'][i])

        cursor.execute(insert_query)
        db_connection.commit()
        time.sleep(0.001)

    count = cursor.execute('select count(*) from todoist')
    print('\nRecords inserted successfully in SQLite DB: ', count.fetchone()[0])  # fetchone() [0]  gives the rowcount


except sqlite3.Error as e:
    print('Failed to insert due to error : ', e)

finally:
    db_connection.close()
    print('\nOperation complete !! Total time taken {} seconds\n\n'.format(round(time.time()-start), 2))

# Found alternate solution at  https://gist.github.com/Maxr1998/82cebde74a4845cb485ac0d5a6dbefa6
