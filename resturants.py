class Resturant:
    """An attempt to model a resturant"""


    def __init__(self, resturant_name, cuisine_type):
        """Initialize the resturant"""
        self.resturant_name = resturant_name.title()
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        """Providing description about the resturant"""
        print(f'{self.resturant_name} offers {self.cuisine_type} cuisine')


    def open_resturant(self):
        """Indacating when the resturant is open"""
        print(f'{self.resturant_name} is now open!')


resturant = Resturant('Tamberma', 'African')

print(f"The name of the resturant is {resturant.resturant_name}")
print(f'They offer {resturant.cuisine_type} cuisine')
print('\n')
resturant.describe_resturant()
resturant.open_resturant()