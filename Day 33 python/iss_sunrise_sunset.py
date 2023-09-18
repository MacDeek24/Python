import requests
from datetime import datetime
from decouple import config
import smtplib
import time


My_gmail = config("GMAIL_USERNAME")
My_Password = config("GMAIL_PASSWORD")

MY_LAT = -12.7465 
MY_LNG = -103.3896

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response)
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-10 <= iss_latitude <= MY_LAT+10 and MY_LNG-10 <= iss_longitude <= MY_LNG+10:
        return True


def is_night():
    parameter = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }
    response = requests.get(url=" https://api.sunrise-sunset.org/json" , params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now().hour
    if time_now >=sunset or time_now <=sunrise:
        return True
    

if is_iss_overhead() or is_night():
    # time.sleep(20)
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=My_gmail,password=My_Password)
            connection.sendmail(
                from_addr=My_gmail,
                to_addrs=My_gmail,
                msg="Subject:Look UP\n\n The Iss Is above the sky."
            )
    except Exception as e:
        print(e)