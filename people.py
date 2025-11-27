kisaki = {
    'first_name':'ayodeji',
    'last_name':'ejiade',
    'age':20,''
    'city':'lagos',
    }
yemi = {
    'first_name':'adeyemi',
    'last_name':'banire',
    'age':21,
    'city':'lagos',
    }
demola = {
    'first_name':'ademola',
    'last_name':'gbadero',
    'age':23,
    'city':'ibadan',
    }
people = [kisaki, yemi, demola]
for person in people:
    name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f'\n{name.title()}, of {city}, is {age} years old')