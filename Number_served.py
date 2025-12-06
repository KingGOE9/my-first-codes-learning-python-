class Resturant:
    """An attempt to model a resturant"""


    def __init__(self, resturant_name, cuisine_type):
        """Initialize the resturant"""
        self.resturant_name = resturant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        """Providing description about the resturant"""
        print(f'{self.resturant_name} offers {self.cuisine_type} cuisine')


    def open_resturant(self):
        """Indacating when the resturant is open"""
        print(f'{self.resturant_name} is now open!')

    def customers_served(self):
        """Displaying the number of customers the resturant has served"""
        print(
            f'{self.resturant_name} has served {self.number_served} customers so far'
        )
    

    def set_number_served(self, served_no):
        """Set the number of customers served to a given value"""
        self.number_served = served_no

    
    def increment_number_served(self, served_update):
        """Add to the number of customers served"""
        self.number_served += served_update



resturant = Resturant('Tamberma', 'African')

print(f"The name of the resturant is {resturant.resturant_name}")
print(f'They offer {resturant.cuisine_type} cuisine')
print('\n')
resturant.describe_resturant()
resturant.open_resturant()
resturant.number_served = 1_500
resturant.customers_served()
resturant.set_number_served(2_300)
resturant.customers_served()
resturant.increment_number_served(800)
resturant.customers_served()