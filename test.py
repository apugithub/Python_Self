import schedule


# import os

def job():
    print("This is a test Program")


# def job_1():
# os.system('python /content/drive/My Drive/Colab Notebooks/Send_Email_Fund_NAV.ipynb')

# schedule.every(5).seconds.do(job_1)
# schedule.every(2).seconds.do(job)
schedule.every(2).seconds.do(job)
# schedule.clear('First_job')  # using unique tag you can stop a job...
# schedule.cancel_job(job)  # This is another way of stopping a job by job name (here 'job') only
# schedule.cancel_job()

while True:
    schedule.run_pending()  # This will start running all the scheduled jobs.
    # time.sleep(10)




