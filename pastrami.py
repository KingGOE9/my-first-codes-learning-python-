sandwich_orders = ['egg','tuna','grilled cheese','club','beef','cuban','pastrami','pastrami','pastrami']
finished_orders = []

print('We are out of pastrami sandwich\n')

while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

while sandwich_orders:
    ordered = sandwich_orders.pop()
    print(f'I made your {ordered.title()} sandwich!')
    finished_orders.append(ordered)

print('\n')

for finished_order in finished_orders:
    print(f'Your {finished_order.title()} sandwich was made')