import requests

api_key = "70ec4ec38d57db6c36b7e1538b409d2f"
OWN_API = "https://api.openweathermap.org/data/2.5/weather"

parameter = {
    "lat":21.145800,
    "lon":79.088158,
    "appid":api_key
}

response = requests.get(OWN_API,params=parameter)
response.raise_for_status()
weather_data = response.json()
condition_code = weather_data["weather"][1]["id"]
if condition_code <= 700:
    print("Bring an umbrella...")