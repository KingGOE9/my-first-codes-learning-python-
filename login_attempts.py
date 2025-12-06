class User:
    """Create a class for Users"""

    def __init__(self, first_name, last_name, age, sex):
        """Initiate the User"""
        self.name = f'{first_name.title()} {last_name.title()}'
        self.age = age
        self.sex = sex.title()
        self.login_attempts = 0


    def describe_user(self):
        """Discribe user information"""
        print(f'{self.name} is a {self.sex}, {self.age} years of age!')


    def greet_user(self):
        """Display User greetings"""
        print(f'Hello {self.name}, how are you this fine morning?')

    
    def logins_attempted(self):
        """Display the number of logins attempted"""
        print(
            f'{self.name} has attempted to login {self.login_attempts} times'
        )


    def increment_login(self, login=1):
        """Track login attempts"""
        self.login_attempts += login

    
    def reset_login_attempts(self):
        """Reset Login attempts value to 0"""
        self.login_attempts = 0


user = User('adeyemi', 'banire', 21, 'male')
user1 = User('ayodeji', 'ejiade', 20, 'male')

print('\n')
user.describe_user()
user.greet_user()
user.increment_login()
user.logins_attempted()
user.increment_login()
user.logins_attempted()
user.increment_login()
user.logins_attempted()
user.increment_login()
user.logins_attempted()
print('\nResetting login attempts')
user.reset_login_attempts()
user.logins_attempted()


print('\n')
user1.describe_user()
user1.greet_user()
user.increment_login()
user.logins_attempted()
user.increment_login()
user.logins_attempted()
print('\nResetting login attempts')
user.reset_login_attempts()
user.logins_attempted()