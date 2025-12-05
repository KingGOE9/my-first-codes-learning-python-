class Resturant:
    """An attempt to model a resturant"""


    def __init__(self, resturant_name, cuisine_type):
        """Initialize the resturant"""
        self.resturant_name = resturant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_resturant(self):
        """Providing description about the resturant"""
        print(f'{self.resturant_name} offers {self.cuisine_type} cuisine')


    def open_resturant(self):
        """Indacating when the resturant is open"""
        print(f'{self.resturant_name} is now open!')

print('\n')
resturant = Resturant('tamberma', 'African')
resturant.describe_resturant()
print('\n')
resturant = Resturant('sora', 'International')
resturant.describe_resturant()
print('\n')
resturant = Resturant("shandy's", 'pasta')
resturant.describe_resturant()