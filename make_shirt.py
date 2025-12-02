def make_shirt(size, print_text):
    """Display shirt size and print text"""
    print(f'A size {size.upper()} shirt with "{print_text}" printed on it')

make_shirt('xxl','The Lord is my shephard')
make_shirt(size='xxl',print_text='The Lord is my shephard')