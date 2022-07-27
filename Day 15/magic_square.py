#A magic Square is a 3*3 grid, such that: It contains ALL 
#the numbers 1 through 9, the sum of each row, each column,
#and diagonal all add up to the same number. In a program, 
#you can simulate a magic square using a two-dimensional 
#list. Write a function that accepts a two-dimensional
#list as input, and determines whether the list is a Magic
#Square or not. Test the function in a program.

import numpy as np
def magic_square_checker(magic_square):
    col_1 = magic_square[:,0]
    col_2 = magic_square[:,1]
    col_3 = magic_square[:,2]
    diag_1 = np.fliplr(magic_square).diagonal()
    diag_2 = np.flipud(magic_square).diagonal()


    if sum(magic_square[0]) == sum(magic_square[1]) == sum(magic_square[2]) == sum(col_1) == sum(col_2) == sum(col_3) == sum(diag_1) == sum(diag_2):
        print('The list provided is a magic square.')
    else:
        print('The list provided is not a magic square.')

def main():
    print('Enter the numbers of your square row by row')
    print('The numbers should be seperated with commas and No space(e.g; 1,2,3)')
    square_1 = list(input('Row 1: ').split(","))
    square_2 = list(input('Row 2: ').split(","))
    square_3 = list(input('Row 3: ').split(","))
    magic_square = [square_1, square_2, square_3]
    magic_square = np.array([list(map(int,i)) for i in magic_square])

    magic_square_checker(magic_square)

main()
