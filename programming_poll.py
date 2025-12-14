polls = []
while True:
    poll = input('\nWhy do you like programming: ')
    polls.append(poll)

    continue_poll = input('Would you like another user to answer (y/n)? ')
    if continue_poll != 'y':
        break


with open('programming_poll.txt', 'a') as prog_poll:
    for poll in polls:
        prog_poll.write(f'{poll}\n')

