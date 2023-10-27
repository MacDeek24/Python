import requests
from decouple import config

sheet_api = config("SHEET_ENDPOINT")
user_name = config("USERNAME")
password = config("PASSWORD")
sheet_Token = config("TOKEN")

first_Name = input("Enter your First Name? :")
last_Name = input("Enter your Last Name?: ")
email=input('Enter your Email ?: ')

sheet_input = {
    "user":{
        "firstName":first_Name,
        "lastName":last_Name,
        "email":email
    }
}

bearer_headers = {
    "Authorization": f"Bearer {sheet_Token}"
    }

response = requests.post(sheet_api , json=sheet_input , headers=bearer_headers)

print(f"Your email is : {email}")