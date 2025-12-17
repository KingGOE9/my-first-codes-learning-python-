def count_common_words(filename, word):
    """Count how many times a particular word appears in a text"""
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        content = contents.lower().count(word)
        num_words = len(contents)
        print(f'{filename} has the word "the" appear {num_words} times')

filename = 'the_saga_of_silver_bend.txt'
count_common_words(filename, 'the')