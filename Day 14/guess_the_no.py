#Guess the number
#You ask a user to guess a number between 1 and 50.
#The user has a maximum of 5 tries. If the user guesses
#wrongly, provide an error message indicating whether 
#their guess was above or below the actual number.
#If the user guesses correctly, congratulate them 
#and show the number of attempts they had. If the
#user exhausts all their tries, and end the game.
#e.g; 
#> enter a number
#user: 1
#> Wrong. The answer is greater than 1
#user: 25
#> Wrong. The answer is less than 25.
#user: 14
#> Wrong.The answer is greater than 14.
#user: 15
#> Correct! You got the right answer in 3 tries.

import random

def guess():
    while True:
        try:
            user_pick = int(input('Enter an integer between 1 and 50: '))
            if user_pick < 1 or user_pick > 50:
                print('The number must be between 0 and 100.\n')
                continue
        except ValueError:
            print('Number must be in figures not letters.\n')
            continue
        break
    return user_pick

def main():
    the_number = random.randint(1, 50)
    user_pick = guess()
    no_of_trials = 0
    for tries in range(4):
        if user_pick < the_number:
            print('Wrong.The answer is greater than', user_pick)
            print()
            user_pick = guess()
            print()
            no_of_trials += 1
        elif user_pick > the_number:
            print('Wrong.The answer is less than', user_pick)
            print()
            user_pick = guess()
            print()
            no_of_trials += 1
        else:
            if no_of_trials > 1:
                print('Correct! You got the number in', no_of_trials, 'tries.')
            else:
                print('Correct! You got the number in', no_of_trials, 'try.')
    else:
        print('Wrong. You have exhausted your tries.\nGame over!')
        print('The number is', the_number)

main()