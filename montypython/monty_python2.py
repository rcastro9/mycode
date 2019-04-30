#!/usr/bin/env python3

round = 0
while(True):
    round = round + 1
    print('Finish the movie title, "Monty Python\'s THe Life of______"')
    answer = input()
    if (answer.lower() == 'brian'):
        print('Correct!')
        break
    elif (answer == 'shruberry'):
        print('You gave the super secret answer!')
        break
    elif(round == 3):
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry! Try again!')

