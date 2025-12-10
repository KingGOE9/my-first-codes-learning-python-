from random import choice

possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winning_picks = []

print('Picking the winning numbers and letters:')
while len(winning_picks) < 4:
    winning_number = choice(possibilities)

    if winning_number not in winning_picks:
        print(f'We pulled a {winning_number}!')
        winning_picks.append(winning_number)

print(f'The final winning ticket is: {winning_picks}')