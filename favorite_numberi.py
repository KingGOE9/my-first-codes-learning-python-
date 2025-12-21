import json

favorite_number = input('What is your favorite number? \n')
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)