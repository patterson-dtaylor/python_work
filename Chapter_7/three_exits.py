# 10/9/19 Exercise: 7-6
# Using the active variable with a while loop
# prompt = "\nEnter the topping you would like on your pizza."
# prompt += "\n(Enter 'quit' when you are finished.)"

# active = True
# while active:
# topping = input(prompt)

# if topping == 'quit':
# active = False

# else:
# print(f"Excellent, I will add {topping} to your pizza.")

# Use a break statement with a loop.
print("Hi, do you need tickets for the prom?")
prompt = "\nEnter the class (freshman, sophmore, junior, or senior) are you in."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    grade = input(prompt)

    if grade == 'quit':
        break

    if grade == 'freshman':
        print("\nSorry you have to be a junior or senior to attend prom.")

    elif grade == 'sophmore':
        print("\nSorry you have to be a junior or senior to attend prom.")

    else:
        print("\nExcellent, you are able to attend prom.")
