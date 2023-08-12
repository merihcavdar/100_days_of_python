travel_log_dict_in_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 20
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {"country": country_visited, "cities_visited": cities_visited, "total_visits": times_visited}
    travel_log_dict_in_list.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log_dict_in_list)
