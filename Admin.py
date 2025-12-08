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


class Admin(User):
    """Represents a specific type of user, an admin"""

    def __init__(self, first_name, last_name, age, sex):
        """Initializing the Admin"""
        super().__init__(first_name, last_name, age, sex)
        self.privileges = []

    def show_privileges(self):
        """Display Admin privileges"""
        print('This is a list of Admin privileges')
        for privilege in self.privileges:
            print(f'- {privilege}')


admin = Admin('adeyemi', 'banire', 21, 'male')
admin.describe_user()
admin.privileges = [
    'can delete posts',
    'can ban user',
    'can add post',
    'can warn user',
    ]
admin.show_privileges()