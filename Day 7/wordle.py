#Wordle
#Task : Make a Wordle game.
#Decription : Wordle is a single player game, in which a user
#is required to guess a 5-letter hidden word in 6 attempts.
#*The user makes a first guess .(e.g: 'Skate').
#*Print out a progress guide, like this. '√⨯⨯√+',
#*'√' Indicates that the letter at that position was guessed correctly.
#*'+' Indicates that the letter at that position is in the hidden word, but in a different position.
#*'⨯' Indicates that the letter at that position is wrong, and isn't in the hidden word.
#This process is repeated until the user either gets the missing word 
#correctly-in which case, or he wins!-, or exhausts his 6 attempts losing.
#The hidden word is generated from a list of 5-letter words hand-coded by you.


import random

def words():
    datastore = ['paint', 'alarm', 'clock', 'death', 'fresh', 'sense', 'false', 'wrong', 'ocean', 'river']
    return datastore

def trial():
    while True:
        try:
            guess = input('Guess the FIVE letters long hidden letter. ')
            return guess
        except Exception:
            print('Incorrect input, try again')
            continue

def check(guess, hidden_word):
    result = []
    for i in range(5):
        if guess[i] == hidden_word[i]:
            result.append('√')
        else:
            if guess[i] in hidden_word:
                result.append('+')
            else:
                result.append('⨯')
    return ''.join(result)
    
def main():
    while True:
        try:
            print("Game instructions:")
            print("1)'√' Indicates that the letter at that position was guessed correctly.")
            print("2)'+' Indicates that the letter at that position is in the hidden word, but in a different position.")
            print("3)'⨯' Indicates that the letter at that position is wrong, and isn't in the hidden word.")
            print("Happy guessing!")
            hidden_word = random.choice(words())
            no_of_trials = 0
            while no_of_trials <6 :
                guess = trial()
                result = check(guess.lower(), hidden_word.lower())
                print(result)
                no_of_trials += 1
                if result == '√√√√√':
                    print('You guessed the hidden word correctly.')
                    break
                else:
                    continue

            else:
                print('You no wise.')
        
        except IndexError:
            print('Ode, your input must be 5 letters long.\n')
            continue

main()