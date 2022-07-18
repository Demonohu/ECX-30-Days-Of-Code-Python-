#Fibonacci
#Using recursion, write a function that prints out the first 'n'
#members of the Fibonacci series. The Fibonacci series is a series
#of integers, starting from 0 and 1, for which each term is the sum
#of the two preceding terms. ie. [0,1,1,2,3,5,8,13,21,...]; OR
#'fib(n+1) = fib(n) + fib(n-1)'

length = int(input('How many numbers long do you want your Fibonacci series to be? '))

def fibonacci(n):
    """
    Takes in a number and prints out the fibonacci series that number long.
    """
    fib_series = [0,1] #Creates a list to add the first two numbers of the fib series
    for no in range(2, n):
        fib_member = fib_series[-1] + fib_series[-2]
        fib_series.append(fib_member)

    return fib_series

print(fibonacci(length))


def fib(n):
    """
    Uses recursion to return the nth number in a fibonacci series
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main(n):
    """
    Prints numbers from the fibonacci series using a recursive function
    """
    for no in range(n):
        print(fib(no))

main(length)