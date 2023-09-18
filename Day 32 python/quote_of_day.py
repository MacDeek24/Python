import smtplib
import datetime as dt
import random
from decouple import config

my_gmail = config('GMAIL_USERNAME')
my_password = config('GMAIL_PASSWORD')
re_email = config('recv_email')


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as qoute_file:
        all_quotes = qoute_file.readlines()
        quotes = random.choice(all_quotes)
    # print(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail , password=my_password)
        connection.sendmail(from_addr=my_gmail ,
                             to_addrs=re_email,
                             msg=f"Subject:Firday Motivation\n\n {quotes}")
