# 10/1/19 Exercise 3-8: Using sorted, reverse, and sort to modify a list of places I would like to see.
locations = ['Nova Scotia', 'London', 'New Zealand', 'Iceland', 'Badlands']

print("Here is the orginial list.")
print(locations)

print("\nHere is the list alphabetized.")
print(sorted(locations))

print("\nHere is the orginial list.")
print(locations)

print("\nHere is the list in reverse order.")
print(sorted(locations, reverse=True))

print("\nHere is the orginial list.")
print(locations)

print("\nHere is the orginial list reverse.")
locations.reverse()
print(locations)

print("\nHere is the orginial list.")
locations.reverse()
print(locations)

print("\nHere is the list organized alphabetized.")
locations.sort()
print(locations)

print("\nHere is the list alphabetized in reverse order.")
locations.sort(reverse=True)
print(locations)
