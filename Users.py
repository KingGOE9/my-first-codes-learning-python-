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


user = User('adeyemi', 'banire', 21, 'male')
user1 = User('ayodeji', 'ejiade', 20, 'male')

print('\n')
user.describe_user()
user.greet_user()


print('\n')
user1.describe_user()
user1.greet_user()