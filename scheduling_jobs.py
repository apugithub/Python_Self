import schedule
import os

def job():
    print("This is a test Program")

def job_1():
    os.system('python AM_PM.py')

schedule.every(5).seconds.do(job)
# some other variations
schedule.every().hour.do(job).tag('First_job', 'test')
schedule.every().day.at("12:25").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().thursday.at("19:15").do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
schedule.every(2).seconds.do(job)

schedule.clear('First_job')  # using unique tag you can stop a job...
schedule.cancel_job(job)  # This is another way of stopping a job by job name (here 'job') only

while True:
    schedule.run_pending()  # This will start running all the scheduled jobs.
    schedule.
    #time.sleep(10)
