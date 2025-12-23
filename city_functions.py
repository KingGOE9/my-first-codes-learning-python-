def get_formatted_city_details(city, country, population=''):
    """Generate a neatly formatted city and country name"""
    if population:
        city_detail = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_detail = f"{city.title()}, {country.title()}"
    return city_detail
