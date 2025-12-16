file_names = ['cats.txt', 'dogs.txt']
for file in file_names:
    
    try:
        with open(file) as f:
            content = f.read()
            
    except FileNotFoundError:
        pass

    else:
        print(f'\nReading file: {file}')
        print(content)