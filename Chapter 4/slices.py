# 10/2/19 Exercise 4-10: Using slices to print messages
# about the certian parts of a list.
players = ['charles', 'martina', 'micheal', 'florence', 'eli']

print("The first three players on the list are:")
for player in players[:3]:
    print(player.title())

print("Three players from the middle of the list are:")
for player in players[1:4]:
    print(player.title())

print("The last three players on the list are:")
for player in players[2:6]:
    print(player.title())
