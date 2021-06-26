# Method 1

stuff = None
fail_condition = None

while True:
    stuff()
    if fail_condition:
        break

'''while True:
        a = service.tasks().list(tasklist=tasklistid, maxResults=100, pageToken=pagetoken).execute()

        # pageToken = Token specifying the result page to return. (Optional)

        try:  # If Task list is not empty
            for i in range(len(a['items'])):
                task_name_id['Task_Name'].append(a['items'][i]['title'])
                task_name_id['Task_ID'].append(a['items'][i]['id'])
        except Exception:
            return None

        pagetoken = a.get('nextPageToken')
        if pagetoken == None:
            break'''


# Method 2

stuff()
while not fail_condition:
    stuff()


# Method 3:  # This way we can safely use try/except block

first_pass = True
while first_pass or condition:
    first_pass = False
    do_stuff()

# Example of Method 3

pagetoken = 6
first_pass = True

# Lets say, we have to iterate 1st time.. from 2nd iteration onwards pagetoken has to be > 3. So we need do-while loop
# The below loop is doing the same as do-while loop
while first_pass or pagetoken > 3:
    print(first_pass, pagetoken)
    first_pass = False
    pagetoken = pagetoken - 1

