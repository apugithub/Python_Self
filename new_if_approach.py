def quiz(grade):
    if grade> 50:
        outcome = "passed"
    else:
        outcome = 'failed'
    print("You", outcome, "with the grade of ", grade)

quiz(60)

def quiz1(grade):   # New if approach
    outcome = "successed" if grade > 40 else "failed"
    print("You", outcome, "with the grade of ", grade)

quiz1(30)