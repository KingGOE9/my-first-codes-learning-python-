from random import choice


def make_winning_ticket(possibilities):
    """Make a wining ticket from a set of possibilities"""
    winning_ticket = []

    while len(winning_ticket) < 4:
        winning_pick = choice(possibilities)
        if winning_pick not in winning_ticket:
            winning_ticket.append(winning_pick)

    return winning_ticket

def check_ticket(new_ticket, winning_ticket):
    """Check if elements in played tickets are in winning tickets"""

    for element in new_ticket:
        if element not in winning_ticket:
            return False
        
    return True

def make_new_ticket(possibilities):
    """Make a new ticket from a set of possibilities"""
    new_ticket = []

    while len(new_ticket) < 4:
        winning_pick = choice(possibilities)
        if winning_pick not in new_ticket:
            new_ticket.append(winning_pick)

    return new_ticket


possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winning_ticket = make_winning_ticket(possibilities)

plays = 0
won = False
max_tries = 1_000_000

while not won:
    new_ticket = make_new_ticket(possibilities)
    won = check_ticket(new_ticket,winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

    

if won:
    print('You have Won the Lottery')
    print(f'Your Ticket: {new_ticket}')
    print(f'Winning Ticket: {winning_ticket}')
    print(f'It only took you {plays} tries')

else:
    print('You have Lost the lottery')
    print(f'Your Ticket: {new_ticket}')
    print(f'Winning Ticket: {winning_ticket}')
    print(f'You have tried {plays} times')
    