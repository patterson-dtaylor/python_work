# 10/2/19 Exercise 4-11: Using the pizza list, add and copy items to the list.
my_pizzas = ['cheese', 'veggie', 'stuffed crust']
friend_pizzas = my_pizzas[:]

my_pizzas.append('thin crust')
friend_pizzas.append('meat lovers')

print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy freind's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
