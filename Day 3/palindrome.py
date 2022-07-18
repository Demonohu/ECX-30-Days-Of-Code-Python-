#Palindromic numbers
#A palindrome is a word that reads the same way forward and backward. (e.g Tenet, 101101) 
#Write a function that prints out all Palindromic numbers less than a given input,
#and returns the total number of palindromes found.
#E.g: f(500) would print all the palindromic numbers less than 500,
#as well as the total number of palindromes less than 500.

working_number = int(input("Enter an integer to work with: "))
#Get an integer from the user.

def palindrome(no):
    """
    This takes an integer as a parameter, checks for all the palindromes
    lesser than the integer using list slicing method to reverse the nuumbers,
    prints all the palindromes and return their total number
    """
    if no >= 10: #Numbers lesser than 10 can't have palindromes
        palindromes_list = [] #Creates an empty list to store the palindromes
        for i in range(10, no):
            if i == int(str(i)[:: -1]) : #Checks if a number is a palindrome by using list slicing.
                palindromes_list.append(i)
            
        print(palindromes_list)
        print('The total number of palindromes in', no, 'is', len(palindromes_list))

    else:
        print('Numbers less than 10 do not have palindromes.')
        palindromes_list = []

        return palindromes_list

palindrome(working_number)

def palindrome2(no):
    """
    This takes an integer as a parameter, checks for all the palindromes
    lesser than the integer using reversed() method and .join to reverse the nuumbers,
    prints all the palindromes and return their total number
    """
    if no >= 10: #Numbers lesser than 10 can't have palindromes
        palindromes_list = [] #Creates an empty list to store the palindromes
        for i in range(10, no):
            i_rev = list(reversed(str(i))) #Reverses a number using reversed()
            if i == int(''.join(i_rev)) : 
            #Changes list to str using .join(), then to int and checks if reversed number is a palindrome
                palindromes_list.append(i)
            
        print(palindromes_list)
        print('The total number of palindromes in', no, 'is', len(palindromes_list))

    else:
        print('Numbers less than 10 do not have palindromes.')
        palindromes_list = []

        return palindromes_list

palindrome2(working_number)