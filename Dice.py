from random import randint

class Dice:
    """A class to model a die"""

    def __init__(self, sides = 6):
        """Initialize the Die"""
        self.sides = sides

    def roll_die(self):
        """Simulate a die rolling"""
        return randint(1, self.sides)

sides6 = Dice()
results = []
print('Results of a 6 sided die rolled 10 times')
for die_roll in range(10):
    result = sides6.roll_die()
    results.append(result)
print(results)

sides10 = Dice(sides = 10)
results = []
print('Results of a 6 sided die rolled 10 times')
for die_roll in range(10):
    result = sides10.roll_die()
    results.append(result)
print(results)

sides20 = Dice(sides = 20)
results = []
print('Results of a 6 sided die rolled 10 times')
for die_roll in range(10):
    result = sides20.roll_die()
    results.append(result)
print(results)