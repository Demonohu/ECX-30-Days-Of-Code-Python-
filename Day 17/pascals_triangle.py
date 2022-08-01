#Pascals Triangle
#An easy one. Write a function that prints out the first 
#'n' rows of Pascal's Triangle. Where 'n' is an integer 
#taken as an argument of the function.


def pascal_triangle(n):
    """
    Prints Pascal's Triangle using binomial coefficient.
    """
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')

        #first element is always 1
        C = 1
        for j in range(1, i+1):

            #first value in a line is always 1
            print(' ', C, sep='', end='')

            #using Binomial Coefficient
            C = C*(i-j)//j
        print()



if __name__ == '__main__':
    isValid = True
    while isValid:
        try:
            print('Abeg try to not enter a number greater than 20. Your choice sha.')
            n = int(input('How many rows of the Pascal triangle do you want to print: '))
            break
        except ValueError:
            print('\n Enter an integer.')
            continue
    pascal_triangle(n)