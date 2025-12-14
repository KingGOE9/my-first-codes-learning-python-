guest = input('Please input your name: ')

with open('guest.txt', 'w') as guests:
    guests.write(guest)
    