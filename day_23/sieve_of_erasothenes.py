#Sieve of Erasothenes
#The sieve of erasothenes is an ancient algorithm for finding all primes less than a given value, n. 
#It operates as follows.
#1) Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
#2) Initially, let p equal 2, the smallest prime number.
#3) Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list
#(these will be 2p, 3p, 4p, ..., the p itself should not be marked.)
#4) Find the smallest number in the list greater than p that is not marked.
#If there was no such number, stop. Otherwise, let p now equal this new number
#(which is the next prime), and repeat from step 3.
#5) When the algorithm terminates, the numbers remaining not marked in the list are all primes below n.
#6) (See more: Sieve of Eratosthenes).
#Using the Sieve of Eratosthenes (as described above), write a function that takes in an integer as input,
#and returns a list containing all primes less than that input number.


def sieve_of_eratosthenes(n):
    list_of_integers = [i for i in range(2, n)]
    p = list_of_integers[0]
    for i in list_of_integers:
        if i % p == 0 and i != p:
            list_of_integers.remove(i)

    for y in list_of_integers:
        if p < y:
            p=y
            for i in list_of_integers:
                if i%p == 0 and i !=p:
                    list_of_integers.remove(i)
    print(list_of_integers)


if __name__ == '__main__':
    isValid = False
    while not isValid:
        no = input('Enter a number: ')
        if no.isdigit():
            isValid = True
        else:
            print('\nNumber should be in digit.')
    no = int(no)
    sieve_of_eratosthenes(no)
