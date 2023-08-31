travel_log = [
    {
        "country":"France",
        "visited": 12,
        "cities":["paris", "lille", "dijon"],
    }, 
    {
        "country": "Germany",
        "visited":5,
        "cities":["berlin", "hamburg", "stuttgart"],
        
    }
]

def add_new_country(country_visited, time_visited, cities_visited):
    new_country = {}
    new_country["country"]=country_visited
    new_country["visited"]=time_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["moscow", "saint petersburg"])
print(travel_log)