import json


try:
    with open('favorite_number.json') as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input('What is your favorite number? \n')
    with open('favorite_number.json', 'w') as f:
        json.dump(favorite_number, f)
    print('Thank you, I will remember that!')
else:
    print(f"I know your favorite number! It's {favorite_number}")


    
