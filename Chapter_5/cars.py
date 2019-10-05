# 10/3/19 Using if statements to set the conditional statment to BMW
# Then printing the list in title capital letters.
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
