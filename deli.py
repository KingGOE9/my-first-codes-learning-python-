sandwich_orders = ['egg','tuna','grilled cheese','club','beef','cuban']
finished_orders = []
while sandwich_orders:
    ordered = sandwich_orders.pop()
    print(f'I made your {ordered.title()} sandwich!\n')
    finished_orders.append(ordered)
for finished_order in finished_orders:
    print(f'\nYour {finished_order.title()} sandwich was made')