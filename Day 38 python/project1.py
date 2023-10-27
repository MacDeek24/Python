# Exercise Tracking with Google sheet

import requests
from datetime import datetime
from decouple import config


sheet_endpoint = config("SHEET_ENDPOINT")
sheet_username = config("USERNAME")
sheet_pass = config("PASSWORD")
sheet_Token = config("TOKEN")


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# print(today_date)
# print(now_time)

sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": "Running",
            "duration": "30 min",
            "calories": "250"
        }
  }

bearer_headers = {
    "Authorization": f"Bearer {sheet_Token}"
    }


sheet_response = requests.post(sheet_endpoint, json=sheet_inputs , headers=bearer_headers)
print(sheet_response)