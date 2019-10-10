# 10/9/19 Exercise 7-8:
sandwich_order = [
    'veggie',
    'pastrami',
    'turkey on rye',
    'pastrami',
    'peanut butter and jelly',
    'pastrami',
    'fried balogna'
]
finished_sandwiches = []

print("Sorry, we have ran out of pastrami.")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    finished_sandwich = sandwich_order.pop()

    print(f"I have made your {finished_sandwich}.")
    finished_sandwiches.append(finished_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
