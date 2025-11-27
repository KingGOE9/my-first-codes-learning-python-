cities = {
    'tokyo' : {
        'country':'Japan',
        'population': '37 million',
        'fact':'Largest metropolitan area in the world'
        },
    'lagos': {
        'country':'Nigeria',
        'population':'22 million',
        'fact':'Fastest growing city in the world',
        },
    'sao paulo': {
        'country':'Brazil',
        'population':'22 million',
        'fact':'Largest economy in the southern hemisphere',
        },
}
for city, information in cities.items():
    print(f"\nHere's some information about {city.title()}")
    for key, value in information.items():
        print(f' - {key.title()} : {value}')