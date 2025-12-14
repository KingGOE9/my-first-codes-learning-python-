print('(Enter quit to exit)')
while True:
    guest_name = input('Please enter your name: ')
    if guest_name == 'quit':
        break
    else:
        print(f'Hello {guest_name.title()}, welcome.')
    with open('guest_book.txt','a') as guest_book:
        guest_book.write(f'{guest_name}\n')
