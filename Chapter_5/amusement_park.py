# 10/5/19: Using if-elif-else Statements.
age = 66
# More concise way of code.
if age <= 4:
    price = 0
elif age < 18:
    price = 25
elif age <= 65:
    price = 40
elif age > 65:
    price = 20
print(f"Your admission cost is ${price}.")
