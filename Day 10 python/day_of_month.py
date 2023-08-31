def is_leap(year):
    return year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0)
    
def day_in_month(year,month):
    if month > 12 or month<1:
        return "Invalid month"
    month_day=[31, 28, 31, 30, 31, 30, 31, 31 ,30, 31, 30, 31 ]
    if is_leap(year) and month == 2:
        return 29
    return month_day[month-1]

year = int(input("Entre A year : "))
month = int(input("Entre A month : "))
day = day_in_month(year, month)
print(day)