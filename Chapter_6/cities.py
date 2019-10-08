# 10/7/19 Exercise 6-11: Dictionaries within a Dictionary:
cities = {
    'atlant': {
        'country': 'united states',
        'population': '3 million',
        'fact': 'hollywood of the south',
    },

    'bangkok': {
        'country': 'thailand',
        'population': '8 million',
        'fact': 'most cars per citizen',
    },

    'amsterdam': {
        'country': 'netherlands',
        'population': '821 thousand',
        'fact': 'the city where anything goes',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"Country: {country.title()}")
    print(f"Population: {population.title()}")
    print(f"Fun Fact: {fact.title()}")
