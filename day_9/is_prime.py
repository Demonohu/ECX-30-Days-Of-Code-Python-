#Is Prime
#Task: Write a function that takes an integer as input
#and determines whether it is a prime number or not.

while True:
    try:
        number = int(input('Enter an integer greater than 0: '))
        if number == 0:
            print('\nNumber must be greater than 0')
            continue
        elif number < 0:
            print('\nNumber must be positive.')
            continue
        break
    except ValueError:
        print('\nEnter a figure not letters: ')
        continue


def is_prime(no):
    status = True
    if no > 2:
        for n in range(2, no-1):
            if no % n == 0:
                status = False

    if status:
        return str(no) + ' is a prime number.'
    else:
        return str(no) + ' is not a prime number.'

print(is_prime(number))
