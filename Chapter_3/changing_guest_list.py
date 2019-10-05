# 9/29/19 Exercise 3-5: Making changes to the guest list from Exercise 3-4.
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
