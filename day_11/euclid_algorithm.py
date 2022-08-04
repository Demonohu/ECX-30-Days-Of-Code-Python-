#Euclid's algorithm(GCD)
#The GCD(Greatest Common Divisor) of two numbers is the
#largest number by which both are divisible. e.g; gcd(42, 18)
#is 6, since 6 is the highest common factor(HCF-same thing
#as GCD) of 42 and 18. Write a program that asks the user
#for two numbers and computes their GCD using Euclid's 
#algorithm. The process is described below: 
#*First, compute the remainder of dividing the larger number 
#by the smaller number with the remainder.
#*Repeat this process until the smaller number equals zero. 
#The GCD is the last value of the larger number.

while True:
    try:
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        break
    except ValueError:
        print("Enter figures, not letters.")
        continue


def euclid(no1, no2):
    if no1 > no2:
        r = no1 % no2
        while r != 0:
            no1 = no2
            no2 = r
            r = no1 % no2
        return no2

    elif no2 > no1:
        r = no2 % no1
        while r != 0:
            no2 = no1
            no1 = r
            r = no2 % no1
        return no1
    else:
        return 'Two equal numbers can not work.'

print(euclid(num1, num2))
