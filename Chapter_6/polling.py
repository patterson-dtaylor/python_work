# 10/6/19 Exercise 6-6: Using loops and if statements to print messages.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'dennis': 'django',
    'taylor': 'python',
    'jack': 'javascript',
    'carrie': '',
    'emaline': '',
    'scout': ''
}

friends = ['carrie', 'emaline', 'scout']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")

    if name not in friends:
        print(f"\t{name.title()}, thanks for taking the poll!")

    if name in friends:
        print(f"\t{name.title()}, you need to take the poll!")
