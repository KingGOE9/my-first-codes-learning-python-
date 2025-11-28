prompt = 'Please enter a pizza topping of your choice '
prompt += "\n(Type quit when you're done): "
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f'I will add {topping} topping to your pizza')
    else:
        break