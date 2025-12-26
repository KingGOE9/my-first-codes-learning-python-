class Employee:
    """A class to model an employee's details"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initializing the employee class"""
        self.first= first_name.title()
        self.last= last_name.title()
        self.salary = annual_salary


    def give_raise(self, salary_raise= 5000):
        """Adds a raise to the annual salary"""
        self.salary += salary_raise


    