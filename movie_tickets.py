prompt = '\nHow old are you?: '
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        price = 0
    elif age >= 3 and age < 13:
        price = 10
    elif age > 12:
        price = 15
    print(f'\nYour movie ticket costs ${price}')
