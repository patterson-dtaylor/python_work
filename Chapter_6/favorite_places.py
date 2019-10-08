# 10/7/19 Exercise 6-9: Creating dictionaries inside dictionaires.
favorite_places = {
    'carrie': ['in bed', 'the mountains', 'trader joes'],
    'emaline': ['cohutta', 'chattanooga', 'camping'],
    'taylor': ['maine', 'amelia island', 'not valdosta']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
