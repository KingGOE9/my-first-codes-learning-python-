favorite_numbers = {
    'kisaki': [67,47,3],
    'light':[29,38,95],
    'nifemi':[16,219,30],
    'king':[22,48],
    'roy':[90,0,4,38],
    }
for names, numbers in favorite_numbers.items():
    print(f"\nThese are {names.title()}'s favorite numbers:")
    for number in numbers:
        print(f'\t - {number}')