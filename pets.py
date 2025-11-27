tiger = {
    'name':'tiger',
    'animal':'dog',
    'owner':'james',
    'eats':'meat',
    }
jessie = {
    'name':'jessie',
    'animal':'parrot',
    'owner':'jessica',
    'eats':'seeds',
    }
bunz = {
    'name':'bunz',
    'animal':'rabbit',
    'owner':'king',
    'eat':'carrots'
    }
pets = [tiger,jessie,bunz]
for pet in pets:
    print(f'\n{pet['name'].title()} informations:')
    for key, value in pet.items():
        print(f'\t{key.title()}:{value.title()}')