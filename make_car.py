def make_car(manufacturer, model_name, **car_details):
    """Build a dictionary containing everything we know about a car"""
    car_details['car_manufacturer'] = manufacturer
    car_details['car_model'] = model_name
    return car_details

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
car = make_car('mercedes', 'AMG', color='black', tow_package=False)
print(car)