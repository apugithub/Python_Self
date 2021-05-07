import todoist as td
from todoist.api import TodoistAPI

api = TodoistAPI('<put API Token here>')

# For Adding Project
for i in range(3):
    #print ('San_{}'.format(151+i))
    api.projects.add('San_{}'.format(151+i))
    api.commit()

#print(project1)