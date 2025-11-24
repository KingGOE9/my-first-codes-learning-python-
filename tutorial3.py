height = input('Input your height: ')
if int(height) <= 1:
    print('You cannot ride, under 1m')
elif int(height) == 7:
    print('You should be in the nba')
elif int(height) > 3:
    print('You cannot ride, over 3m')

else:
    print('Congratulations, you can ride')