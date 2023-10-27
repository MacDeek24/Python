from datetime import datetime, timedelta
import requests
from decouple import config

ORIGIN_CITY_IATA = "LON"
SHEETY_PRICES_ENDPOINT = config("SHEET_ENDPOINT")
AVIATIONSTACK_ENDPOINT = config("FLIGHT_API")
AVIATIONSTACK_API_KEY = config("FLIGHT_KEY")

response = requests.get(url=SHEETY_PRICES_ENDPOINT)
sheet_data = response.json()["prices"]

# print(sheet_data)



response = requests.get(url=SHEETY_PRICES_ENDPOINT)
sheet_data = response.json()["prices"]
# Function to get flight data
def get_flight_data(origin_iata, destination_iata, from_time, to_time):
    params = {
        "access_key": AVIATIONSTACK_API_KEY,
        "dep_iata": origin_iata,
        "arr_iata": destination_iata,
        "dep_date": from_time.strftime("%Y-%m-%d"),
        "arr_date": to_time.strftime("%Y-%m-%d"),
    }

    response = requests.get(AVIATIONSTACK_ENDPOINT, params=params)
    data = response.json()
    return data




tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight_data = get_flight_data(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    print(flight_data)

    # if "data" in flight_data and len(flight_data["data"]) > 0:
    #     lowest_price = min(flight["price"] for flight in flight_data["data"])
    #     # if lowest_price < destination["lowestPrice"]: