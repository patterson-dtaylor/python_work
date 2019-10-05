# 10/3/19: Exercise 5-1: Creating conditional tests to test true and false statments.
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

food = 'pizza'
print("\nIs food == 'pizza'? I predict True.")
print(food == 'pizza')

print("\nIs food == 'potato chips'? I predict False.")
print(food == 'potato chips')

hair = 'brown'
print("\nIs hair == 'brown'? I predict True.")
print(hair == 'brown')

print("\nIs hair == 'black'? I predict False.")
print(hair == 'black')

bathing = 'shower'
print("\nIs bathing == 'bath'? I predict False.")
print(bathing == 'bath')

print("\nIs bathing == 'shower'? I predict True.")
print(bathing == 'shower')

drink = 'coffee'
print("\nIs drink == 'coffee'? I predict True.")
print(drink == 'coffee')

print("\nIs the breakfast drink == 'orange juice'? I predict False.")
print(drink == 'organge juice')

mothers = ['Carrie', 'carrie', 'Traci', 'honey', 'Trish', 'Marie']
for mother in mothers:
    if mother == mother.lower():
        print(mother)

age = 25
if age < 21:
    print("\nThat is not the correct age to drink in this country.\nPlease try again when you're old enough.")
if age <= 21:
    print("\nThat is not the correct age to drink in this country.\nPlease try again when you're old enough.")
if age > 21:
    print("\nThat is the correct age to drink in this country.\nPlease don't drink and drive.")
if age >= 21:
    print("\nThat is the correct age to drink in this country.\nPlease don't drink and drive.")

failing_students = ['taylor', 'carrie', 'dennis', 'scout']
user = 'emaline'
user1 = 'taylor'

if user not in failing_students:
    print(f"\n{user.title()}, you can go on the field trip!")
if user1 in failing_students:
    print(f"\nSorry {user1.title()}, you are a failing student.  You will not go on the field trip.")
