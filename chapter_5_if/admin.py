# 5-8: Hello Admin
# Make a list of five or more usernnames, including the name 'admin'. 
# Imagine you are writing code that will print a greeting to each user after they log in to a website. 
# Loop through the list, and print a greeting to each user:

# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Eric, thank you for loggin in again.

usernames = ['Eric', 'wiLLie', 'ADMIN', 'eRin', 'ever']

for username in usernames:
    if username.lower() == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again!")