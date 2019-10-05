# 9/29/19 Exercise 3-6: A bigger table and more guests!
guest_list = ['Mr. Obama', 'Mr. Stienbeck', 'Mrs. Ginsburg']
invitation1 = f"{guest_list[0]}, I am having a dinner party, and I would love for you to make it."
invitation2 = f"{guest_list[1]}, I am having a dinner party, and I would love for you to make it."
invitation3 = f"{guest_list[2]}, I am having a dinner party, and I would love for you to make it."

print(invitation1)
print(invitation2)
print(invitation3)

invitation_change = f"Dear {guest_list[0]} and {guest_list[2]}, {guest_list[1]} couldn't make it."
print(invitation_change)

del guest_list[1]
guest_list.insert(1, 'Mr. Chappelle')
print(guest_list)

invitation1 = f"{guest_list[0]}, I am having a dinner party, and I would love for you to make it."
invitation2 = f"{guest_list[1]}, I am having a dinner party, and I would love for you to make it."
invitation3 = f"{guest_list[2]}, I am having a dinner party, and I would love for you to make it."

print(invitation1)
print(invitation2)
print(invitation3)

more_guests = f"{guest_list[0]}, {guest_list[1]}, and {guest_list[2]}, \nI have found a new table and will be adding three more guests!"
print(more_guests)

guest_list.insert(0, 'Mr. Bourdain')
guest_list.insert(2, 'Mrs. Lee')
guest_list.append('Mr. Poe')
print(guest_list)

invitation1 = f"{guest_list[0]}, I am having a dinner party, and I would love for you to make it."
invitation2 = f"{guest_list[1]}, I am having a dinner party, and I would love for you to make it."
invitation3 = f"{guest_list[2]}, I am having a dinner party, and I would love for you to make it."
invitation4 = f"{guest_list[3]}, I am having a dinner party, and I would love for you to make it."
invitation5 = f"{guest_list[4]}, I am having a dinner party, and I would love for you to make it."
invitation6 = f"{guest_list[5]}, I am having a dinner party, and I would love for you to make it."

print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6)
