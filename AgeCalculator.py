def AgeCalculator(y,m,d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days/365.25)
    print(age)
AgeCalculator(1997,8,10)