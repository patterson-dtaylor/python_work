# 10/6/19 Exercise 6-1: Using a dictionary to store personal information
# 10/7/19 Exercise 6-7: Using multiple dcitonaries in a list
person_0 = {
    'first_name': 'scout',
    'last_name': 'patterson',
    'age': 2,
    'city': 'valdosta',
}
person_1 = {
    'first_name': 'emaline',
    'last_name': 'patterson',
    'age': 10,
    'city': 'valdosta',
}
person_2 = {
    'first_name': 'traci',
    'last_name': 'patterson',
    'age': 54,
    'city': 'cohutta',
}

persons = [person_0, person_1, person_2]

for person in persons:
    print(f"\n{person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tShe is {person['age']} years old.")
    print(f"\tShe lives in {person['city'].title()}.")
