# 10/6/19 Exercise 6-5: Create a dicitonary with rivers and countries.
# Using loops to print a sentence about each key and value.
# Using the key method, only print keys.
# Using the value method, only print values.
rivers = {
    'nile': 'egypt',
    'mississppi': 'united states',
    'amazon': 'brazil'
}

for river, country in rivers.items():
    print(f"The {river.title()} is located in {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
