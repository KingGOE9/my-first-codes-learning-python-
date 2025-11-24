Glossary = {'lists':'Used to store data of related ilems',
            'string':'A series of characters',
            'comment':'A note the interpreter ignores',
            'dictionary':'A collection of key-value pairs' ,
            'loop':'work through a collection of items, one at a time',
            'tab': 'Used to indent on new lines',
            'Glossary' : 'Also known as a dictionary',
            'title' : 'Used to capitalize the first letter of words'
            }
for words, meaning in Glossary.items():
    print(f'{words.title()}:\n {meaning}\n')