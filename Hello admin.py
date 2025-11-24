usernames = ['daniel','david','tolani','tobe','munirat','admin']
if usernames:
    for username in usernames:
        if username=='admin':
            print('Hello admin, would you like to see status report?')
        else:
            print(f'Hello {username}, thank you for logging in again\n')
else:
    print('We need to find some users!')