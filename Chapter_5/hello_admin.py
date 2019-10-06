# 10/5/19 Exercise 5-8: Within a list of usernames, loop a message to all.
# If there is an admin user, print a different message.
usernames = ['carrie', 'emaline', 'scout', 'nikki', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")

# Exercise 5-9: No user line.
# else:
    # print("We need to get some users!")
