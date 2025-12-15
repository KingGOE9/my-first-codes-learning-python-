print("Input two numbers you would like to add together")
print('(Enter "q" at any point to quit)')
while True:
    first_number = input("First number: \n")
    if first_number == 'q':
        break
    try:
        first_number = int(first_number)
    except ValueError:
        print('You have entered an invalid input, try entering a valid number\n')
        continue
    else:
        first_number = int(first_number)

    second_number = input("Second number: \n")
    if second_number == 'q':
        break
    try:
        second_number = int(second_number)
    except ValueError:
        print('You have entered an invalid input, try entering a valid number\n')
        continue
    else:
        second_number = int(second_number)

    sum = first_number + second_number
    print(f'{sum}\n')
