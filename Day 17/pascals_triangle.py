#Pascals Triangle
#An easy one. Write a function that prints out the first 
#'n' rows of Pascal's Triangle. Where 'n' is an integer 
#taken as an argument of the function.


isValid = True
while isValid:
    try:
        n = int(input('How many rows of the Pascal triangle do you want to print: '))
        break
    except ValueError:
        print('\n Enter an integer.')
        continue

def pascal_triangle(n):
    triangle = ''
    for i in range(n-1):
        i


pascal_triangle(n)
