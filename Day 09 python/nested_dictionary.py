#nested dictionary
#Nesting List In A dictionary
travel_log = {
    "France":["paris", "lille", "dijon"],
    "Germany": ["berlin", "hamburg", "stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
    "France":{"cities_visited":["paris", "lille", "dijon"], "total_visited": 12},
    "Germany": {"cities_visited":["berlin", "hamburg", "stuttgart"],"total_visited":5},
}

#Nesting Dictionary in a List
travel_log = [
    {
        "country":"France",
        "cities_visited":["paris", "lille", "dijon"],
        "total_visited": 12,
    },
    {
        "country": "Germany",
        "cities_visited":["berlin", "hamburg", "stuttgart"],
        "total_visited":5,
    }
]