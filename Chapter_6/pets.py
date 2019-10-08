# 10/7/19 Exercise 6-8: Dictionaries in a list and printing info
pet_0 = {
    'kind_of_pet': 'dog',
    'breed': 'blue heeler',
    'name_of_pet': 'nikki',
    'owners_name': 'taylor and carrie',
}

pet_1 = {
    'kind_of_pet': 'puma',
    'breed': 'mountain lion',
    'name_of_pet': 'nala',
    'owners_name': 'emaline'
}

pet_2 = {
    'kind_of_pet': 'fish',
    'breed': 'baracuda',
    'name_of_pet': 'chomper',
    'owners_name': 'scout'
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"\n{pet['name_of_pet'].title()}")
    print(f"\tKind of animal: {pet['kind_of_pet'].title()}")
    print(f"\tBreed: {pet['breed'].title()}")
    print(f"\tOwner's name: {pet['owners_name'].title()}")
