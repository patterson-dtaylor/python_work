# 10/8/19 The while loop in action
# current_number = 0
# while current_number < 10:
# current_number += 1
# if current_number % 2 == 0:
# continue

# print(current_number)

# 10/8/19 Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
# You leave this empty if will create a loop forever.
    x += 1
