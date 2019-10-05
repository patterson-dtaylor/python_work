# 10/3/19: Checking whether a value is not in a list.
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a reponse if you wish.")
