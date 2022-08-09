#Using Python, create a game with the following rules:
#1) A(randomly generated) basic algebraic expression is displayed onto the screen.(e.g; 36×47, or 117÷9, etc)
#2) The user is required to provide an answer to the expression within 10 seconds.
#3) If the user provides a RIGHT answer, he gains {10x(the number of seconds left)} points
#4) If the user provides a WRONG answer, or the time elapsed, the player loses a life.
#5) At the start of the game, the player provides his name, and begins playing with 3 lives.
#6) The player loses once he has exhausted his 3 lives.
#Note:
#-Only +,-,× operations are. In the case of a division operation, the two numbers generated MUST be divisible.

import random
import time

class Game:
    def __init__(self, lives, points):
        self.lives = lives
        self.points = points

    def set_algebraic_question(self):
        operators = ('+', '-', '÷', 'x')
        operator = random.choice(operators)
        if operator == '+':
            answer = a + b
            question = (str(a), '+' ,str(b))
        elif operator == '-':
            answer = a - b
            question = (str(a), '-' ,str(b))
        elif operator == 'x':
            answer = a * b
            question = (str(a), 'x' , str(b))
        else:
            while a%b != 0:
                a = random.randint(1, 50); b = random.randint(1, 50)
            else:
                answer = a // b
                question = (str(a), '÷' , str(b))

        return question, answer

    def get_user_answer(self):
        question, __ = self.set_algebraic_question()
        t1 = time.time()
        print(''.join(question))
        user_answer = input('Your answer: ')
        t2 = time.time()
        enter_time = t2 - t1
        time_left = 10 - int(enter_time)
        return user_answer, time_left

    def check_answer(self):
        __, answer = self.set_algebraic_question()
        user_answer, time_left = self.get_user_answer()
        if time_left > 0:
            if int(user_answer) == answer:
                self.points += time_left
                print('Correct!', time_left, 'points added!')
            else:
                self.lives -= 1
                print('Wrong. You have ', self.lives, ' lives left.', sep='')
                print(answer)
        else:
            self.lives -= 1
            print('Time elapsed. You have ', self.lives, ' lives left.', sep='')
            
            


if __name__ == '__main__':
    print('Welcome to the coolest game ever!')
    print('The rules of this game.')
    print('* You start the game with three lives and zero point')
    print("* You have 10 seconds to answer each question. You lose a life if you don't answer on time.")
    print("* You lose a life if you give an incorrect answer.")
    print("* If you give the correct answer, you gain 10-the time taken for you to answer points.")
    print('Goodluck.')
    print('The game starts now!')
    print()
    player = input('Enter your name: ')
    player = Game(3, 0)
    while player.lives > 0:
        player.check_answer()
    print('You finished with', player.points, 'points.')
