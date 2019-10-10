# 10/8/19 Exercise 7-4: While loops with pizza toppings.
prompt = "\nEnter the topping you would like on your pizza."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    else:
        print(f"Excellent, I will add {topping} to your pizza.")
