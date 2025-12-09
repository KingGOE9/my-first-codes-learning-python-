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


class IceCreamStand(Resturant):
    """Represents a type of Resturant, specific to an Ice Cream Stand"""


    def __init__(self, resturant_name, cuisine_type = 'Ice Cream'):
        """Initialize attributes of parent class"""
        super().__init__(resturant_name, cuisine_type)
        self.flavors = []

    def available_flavors(self):
        """Display available flavors"""
        print('\nThese are the flavors we have available:')
        for flavor in self.flavors:
            print(f'- {flavor.title()}')