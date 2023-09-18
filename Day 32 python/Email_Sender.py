import smtplib
from decouple import config

my_gmail = config('GMAIL_USERNAME')
my_password = config('GMAIL_PASSWORD')
re_email = config('recv_email')


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_gmail , password=my_password)
    connection.sendmail(from_addr=my_gmail , to_addrs=re_email, msg="Subject:Hello\n\n This is a Welcome message ...")

