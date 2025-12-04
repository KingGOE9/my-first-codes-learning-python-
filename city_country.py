def city_country(city,country):
    """Display formatted city and country"""
    location = f'{city}, {country}'
    return location.title()

city=city_country('abuja','nigeria')
print(city)
city=city_country('new york', 'america')
print(city)
city=city_country('sydney','australia')
print(city)
