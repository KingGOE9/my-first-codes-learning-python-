def make_sandwich(*fillings):
    """Collect and display items in a sandwich"""
    print('\nYou have ordered a sandwich with the following fillings:')
    for filling in fillings:
        print(f'-{filling}')

make_sandwich('bacon','cheese','egg','beef','cabbage')
make_sandwich('lettuce','tomatoes','onions')
make_sandwich('chicken','mayonaise')