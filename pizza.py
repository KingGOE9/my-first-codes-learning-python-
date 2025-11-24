pizza= ['pepperoni', 'chicken', 'beef', 'veggie']
for pizzas in pizza:
    print(f'I love eating {pizzas} pizza\n')
print('I really love pizza\n')

friend_pizza=pizza[:]
pizza.append('pineapple')
friend_pizza.append('spicy')
for pizzas in pizza:
    print(f'My favorite pizzas are {pizzas}\n')
for fpizzas in friend_pizza:
    print(f"My friend's favorite pizzas are {fpizzas}\n")