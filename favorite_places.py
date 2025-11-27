favorite_places = {
    'yemi' : ['switzerland','norway','japan'],
    'kisaki': ['america','london'],
    'demola' : ['paris','seychelles','sweden'],
    }
for name, places in favorite_places.items():
    print(f'\nThese are {name.title()} favorite places:')
    for place in places:
        print(f'\t - {place.title()}')