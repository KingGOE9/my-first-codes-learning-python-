class User:
    """Create a class for Users"""

    def __init__(self, first_name, last_name, age, sex):
        """Initiate the User"""
        self.name = f'{first_name.title()} {last_name.title()}'
        self.age = age
        self.sex = sex.title()


    def describe_user(self):
        """Discribe user information"""
        print(f'{self.name} is a {self.sex}, {self.age} years of age!')


    def greet_user(self):
        """Display User greetings"""
        print(f'Hello {self.name}, how are you this fine morning?')

class Privileges:
    """Represents User Privileges"""

    def __init__(self, privileges=[]):
        """Initializing the user privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Display Admin privileges"""
        if self.privileges:
            print('This is a list of Admin privileges')
            for privileges in self.privileges:
                print(f'- {privileges}')
        else:
            print('This User has no privileges')
        
        
class Admin(User):
    """Represents a specific type of user, an admin"""

    def __init__(self, first_name, last_name, age, sex):
        """Initializing the Admin"""
        super().__init__(first_name, last_name, age, sex)
        self.privilege = Privileges()