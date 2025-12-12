file_name = 'learning_python.txt'

print('Reading through the entire file:')
with open(file_name) as file_object:
    content = file_object.read()
print(content)

print('\nLooping over the file object:')
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\nStoring lines in a list:')
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
