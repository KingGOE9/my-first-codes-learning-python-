"""A set of class to model Admins and their privileges"""

from user import User

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