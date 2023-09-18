import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday

print(now)

date_of_birth = dt.datetime(year=1995,month=8,day=21)
print(date_of_birth)
