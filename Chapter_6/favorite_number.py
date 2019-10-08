# 10/6/19 Exercise 6-2: Using a dictionary to poll people's fav number.
favorite_numbers = {
    'carrie': ['12', '4'],
    'scout': ['11', '21'],
    'emaline': ['3', '12'],
    'taylor': ['33', '11'],
    'nikki': ['69', '99'],
}

# 10/7/19 Exercise 6-10: Using a list in a dictionary.
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")
