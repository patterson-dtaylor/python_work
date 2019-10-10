# 10/7/19 Exercise 7-3: Is it a multiple of 10?
number = input("Enter a number, and I'll tell you if it's a mulitple of ten.")
number = int(number)

if number % 10 == 0:
    print(f"\nYes, {number} is a multiple of ten!")
else:
    print(f"\nNo, {number} is not a multiple of ten. Pick again!")
