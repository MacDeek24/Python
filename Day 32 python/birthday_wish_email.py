from datetime import datetime
import pandas
import random
import smtplib
from decouple import config


my_gmail = config('GMAIL_USERNAME')
my_password = config('GMAIL_PASSWORD')

today = datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("Birthday_Wish.csv")


new_dict = { (row["month"] , row["day"]) : row  for(_ , row) in data.iterrows()}

if today_tuple in new_dict:
    birthday_person = new_dict[today_tuple].to_dict()
    file_path = f"letter_{random.randint(1,3)}.txt"
   
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # print(birthday_person.keys(),birthday_person,type(birthday_person))
        # name = birthday_person["name"]
        # print(name,"name")
        contents=contents.replace("[NAME]",birthday_person["name"] )



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail , password=my_password)
        connection.sendmail(from_addr= my_gmail , 
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday\n\n {contents}"
                            )

