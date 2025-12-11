dream_vacation = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name?: ')
    location = input('\nIf you could visit one place in the world, where would you go?: ')

    dream_vacation[name] = location

    repeat = input('\nWould you like another person to respond (yes/no)?: ')
    if repeat == 'no':
            polling_active = False

print('\n')
for name, location in dream_vacation.items():
      print(f'{name.title()} would love to visit {location.title()} on a dream vacation\n')