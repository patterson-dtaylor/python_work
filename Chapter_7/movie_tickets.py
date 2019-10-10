# 10/8/19 Exercise 7-5: Asking age and giving the price of tickets.
print("Welcome to the movies.")
prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("\nYour ticket is free!")

    elif age < 13:
        print("\nYour ticket is $10.")

    else:
        print("\nYour ticket is $15.")
