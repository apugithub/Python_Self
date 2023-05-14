from datetime import date, datetime

today = date.today()


def age_cal(dob):  # DOB is in YYYY-MM-DD format
    # dob = '1989-06-20'
    dob_date_object = datetime.strptime(dob, '%Y-%m-%d').date()  # Converting str to date object
    days_difference = (today - dob_date_object).days   # Converting difference in days
    year = int(days_difference/365)
    return year


print('San age: ', age_cal('1989-06-20'), ' years\n')
print('Mouli age: ', age_cal('1991-06-22'), ' years\n')
print('Dad age: ', age_cal('1952-11-04'), ' years\n')
print('Mom age: ', age_cal('1968-10-12'), ' years\n')
print('Kabita Sar age: ', age_cal('1961-06-16'), ' years\n')
print('Ayandip Sar age: ', age_cal('1987-07-25'), ' years\n')
print('Ayantika Sar Tripathi: ', age_cal('1997-12-07'), ' years')
