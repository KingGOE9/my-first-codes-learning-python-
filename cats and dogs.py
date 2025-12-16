file_names = ['cats.txt', 'dogs.txt']
for file in file_names:
    print(f'\nReading file: {file}')
    try:
        with open(file) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print('This file does not exist')

         


