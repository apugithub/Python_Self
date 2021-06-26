from todoist.api import TodoistAPI
import pandas as pd
import json
import time
from tqdm import tqdm

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
        for i in item_list:
            item = api.items.get_by_id(i)
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
    active_tasks['Priority'].append(items1[i]['priority'])
    time.sleep(0.01)

df = pd.DataFrame(active_tasks).sort_values(by=['Due_Date'], ascending=True)
df.to_json(r'D:/Essentials/Blue Bird ==========/Documents/Todoist/Todoist.json', orient='records', indent=4)

print('\n\n' + 'JSON Backup taken successfully, operation complete !!')


# Found alternate solution at  https://gist.github.com/Maxr1998/82cebde74a4845cb485ac0d5a6dbefa6

