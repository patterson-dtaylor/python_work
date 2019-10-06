# 10/5/19 Exercise 5-10: Checking current usernames with new usernames
# To insure there is no overlap.
current_users = ['carrie', 'emaline', 'scout', 'taylor', 'nikki']

new_users = ['Dennis', 'traci', 'larry', 'SCOUT', 'niKKi']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry {new_user}, you will need to enter a new username.")
    else:
        print(f"Welcome, {new_user.title()}, that username is available!")
