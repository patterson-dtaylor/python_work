# 10/6/19 Using a dictionary to poll people's favorite language.
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# Below is used to find one key and value in the dictionary.
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Use keys() if you only want the keys
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
    # print(name.title())
    # print(f"\nHi {name.title()}.")

    # if name in friends:
        # language = favorite_languages[name].title()
        # print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
    # print("\nErin, please take our poll!")

# If you want to sort the keys use sorted()
# for name in sorted(favorite_languages.keys()):
    # print(f"\n{name.title()}, thank you for taking the poll!")

# If you want to print only values:
# If you only want to see the value once, use set() method.
# print("\nThe following languages have been mentioned.")
# for language in set(favorite_languages.values()):
    # print(language.title())
