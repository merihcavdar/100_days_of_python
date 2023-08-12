# {
#   Key: [List],
#   Key2: {},
# }

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log["Germany"][1])

nested_lists = ["A", "B", ["C", "D"]]
print(nested_lists[2][1])

# nesting dictionary in a dictionary

travel_log_with_visit_count = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 20},
}

print(travel_log_with_visit_count["Germany"]["total_visits"])
print(travel_log_with_visit_count["France"]["cities_visited"][1])

# nesting dictionary in a list

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
print(travel_log_dict_in_list[1]["cities_visited"][2])
