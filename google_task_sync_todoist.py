import json
from google_task_methods import Create_Service
import time
from tqdm import tqdm  # For progress bar
import pandas as pd

start = time.time()

f = open('D:/Essentials/Blue Bird ==========/Documents/Todoist/Todoist.json')
todoist_json = json.load(f)

CLIENT_SECRET_FILE = 'D:/Essentials/Blue Bird ==========/Documents/Todoist/sg1988_client_secret.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

response = service.tasklists().list().execute()
tasklist_name_id = {'Tasklist_Name': [], 'Tasklist_ID': []}
task_name_id = {'Task_Name': [], 'Task_ID': [], 'Task_Due': []}


for i in range(len(response['items'])):
    tasklist_name_id['Tasklist_Name'].append(response['items'][i]['title'])
    tasklist_name_id['Tasklist_ID'].append(response['items'][i]['id'])

tasklistid = tasklist_name_id['Tasklist_ID'][1]  # All tasks will be added to this tasklist


def add_tasklist(tasklist_name):
    service.tasklists().insert(body={'title': tasklist_name}).execute()


def delete_tasklist(tasklist_id):
    service.tasklists().delete(tasklist=tasklist_id).execute()


def show_all_tasks():  # This will show all tasks of the mentioned tasklist id only

    task_name_id['Task_Name'] = []  # Resetting to empty list before show_all_tasks call
    task_name_id['Task_ID'] = []  # Resetting to empty list before show_all_tasks call
    task_name_id['Task_Due'] = []

    pagetoken = None
    first_pass = True

    while first_pass or pagetoken:  # This loop is same as do-while loop
        # First we have to traverse 'a' without specifying pagetoken, that's what the 1st iteration does
        # from 2nd iteration, its making sure 'pageToken' has proper value. So no matter what, the 1st iteration goes
        # through, but from 2nd iterations, condition (pagetoken existence) is checked

        first_pass = False
        a = service.tasks().list(tasklist=tasklistid, maxResults=100, pageToken=pagetoken).execute()

        try:  # If Task list is not empty
            for ii in range(len(a['items'])):
                task_name_id['Task_Name'].append(a['items'][ii]['title'])
                task_name_id['Task_ID'].append(a['items'][ii]['id'])
                task_name_id['Task_Due'].append(a['items'][ii]['due'])
        except Exception:
            return None

        pagetoken = a.get('nextPageToken')


show_all_tasks()  # This method has to run every time, to populate 'task_name_id' dict
print('\nTotal tasks in Google Task before sync: {}'.format(len(task_name_id['Task_ID'])))


def add_task(task_name, due_date):  # Due will be in '2021-05-31T00:00:00.000Z' format
    service.tasks().insert(tasklist=tasklistid, body={'title': task_name, 'due': due_date}).execute()


def delete_task(taskid):
    service.tasks().delete(tasklist=tasklistid, task=taskid).execute()


def import_todoist_tasks():
    # First will cleanup the existing tasks
    print('\nCleaning up process started...')

    try:  # If Task_ID list is not empty
        for i in tqdm(task_name_id['Task_ID']):  # tqdm along with time.sleep is for progress bar only
            service.tasks().delete(tasklist=tasklistid, task=i).execute()
            time.sleep(0.01)

    except Exception as e:
        print('There are issues during cleaning up...: {}'.format(e))

    print('\nCleaning process finished & ToDoIst import started..')
    print('Total tasks in todoist: {}'.format(len(todoist_json)))

    for i in tqdm(range(len(todoist_json))):  # tqdm along with time.sleep is for progress bar only
        task_name = todoist_json[i]['Task_Name']
        task_due_date = todoist_json[i]['Due_Date'] + 'T00:00:00.000Z'  # As per expected date format in Google Task API
        service.tasks().insert(tasklist=tasklistid, body={'title': task_name, 'due': task_due_date}).execute()
        time.sleep(0.01)

    show_all_tasks()
    print('Total tasks added in Google_Task: {}'.format(len(task_name_id['Task_ID'])))


import_todoist_tasks()


def export_googletasks():
    show_all_tasks()  # This is to refresh the tasklist
    df = pd.DataFrame(task_name_id).sort_values(by=['Task_Due'], ascending=True)
    df.to_json(r'D:/Essentials/Blue Bird ==========/Documents/Todoist/GoogleTasks.json', orient='records', indent=4)
    print('\nGoogleTasks exported successfully.')


export_googletasks()

print('\nOperation complete !! Total time taken {} seconds\n\n'.format(round(time.time()-start), 2))

''' To add a google account to use this app, if publishing status is in testing: [in testing, token validity 2 weeks]
    the same account needs to be added in test user of API, for that
    1. login to Google Cloud (where API was registered)==> API & Services ==> OAuth consent screen ==> 
    ADD USERS (in Test users) ==> add the gmail_id of new user 
    
    2. remove pickle file (from from local system) then run the google_task_sync_todoist.py **
    3. Use the link appeared in console to authenticate the app in your account
    ** Only one account can be added in one pickle file
    
To add a google account to use this app, if publishing status is in production): [in prod, token validity no limit]
    No need to add the user, but total 100 users can access the app
    Then follow step 2 & 3 as above
    
    
    
'''

# Fetch all tasks Ref: https://stackoverflow.com/questions/56615087/how-to-return-all-task-with-google-script
