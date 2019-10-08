# 10/6/19 Working with a simple dictionary.
# alien_0 = {'color': 'green', 'points': 5, }

# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You just earned {new_points}!")

# You can delete items from your dictionary like this:
# Be careful using this, remeber once it's gone, it's gone.
# del alien_0['points']

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# Adding to a blank dictionary
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# Modifying a dictionary
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# Alien speed
# alien_0 = {'x_position': 0, 'y_poisition': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
# x_increment = 1
# elif alien_0['speed'] == 'medium':
# x_increment = 2
# else:
# This must be a fast alien.
# x_increment = 3

# The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")

# Nesting a list inside a dictionary
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
# print(alien)

# More realistic example of nesting in a dictionary.
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# To change the color of an alien and make it faster and worth more.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:10]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
