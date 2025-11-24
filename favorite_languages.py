favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

pollees = ['yemi','david','jen','tobe','edward']
for pollee in pollees:
    if pollee in favorite_languages:
        print(f'{pollee.title()}, Thank you for your response\n')
    else:
        print(f'{pollee.title()}, Please participate in the poll\n')