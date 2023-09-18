import requests
from datetime import datetime

MY_LAT = 23.022505
MY_LNG = 72.571365
parameter = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}


response = requests.get(url=" https://api.sunrise-sunset.org/json" , params=parameter)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
Time_now = datetime.now()
print(Time_now.hour)