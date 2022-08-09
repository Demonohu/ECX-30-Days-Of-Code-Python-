#Binary search algorithm.
#'Binary search' is a basic algorithm, used to find the 
#position of a target value within a SORTED LIST. 
#(More details can be found here: Binary search).
#For today's task, write a function that takes in two
#parameters: One list of alphabets, and one character
#to search.
#e.g; f('x', ['m', 'v', 'x', 'u']) in your function:
#1) First check if the input list is sorted, using 
#any method of your preference.
#2) Using BINARY SEARCH ALGORITHM, find the position
#of the input character in the sorted list.
#3) Return the position of the character in the search list.
#4)If the character is not found, return false.



def binary_search(lst, wanted):
    lst.sort()
    print(lst, wanted)
    l = 0; r = len(lst)
    while l <= r:
        m = l+(r-l)//2
        if wanted > lst[m]:
            l = m+1
        elif wanted < lst[m]:
            r = m-1
        else:
            return m
    return -1
    

if __name__ == '__main__':
    isListValid = False
    while not isListValid:
        lst = input('Enter a list of alphabets. Seperate each letter with a space. e.g; (a b c d): ')
        unwanted = '' 
        for i in range(1, len(lst), 2):
            unwanted += lst[i]
        if unwanted == ' '*(len(lst)//2):
            lst = lst.replace(' ', '')
            if lst.isalpha():
                isListValid = True
            else:
                print('\nEnter letters of the alphabet only.')
        else:
            print('\nEach alphabet must be seperated with a space.')
        lst = list(lst)

    isWantedValid = False
    while not isWantedValid:
        wanted = input('Enter a character to search for: ').lower()
        if wanted.isalpha():
            isWantedValid = True
        else:
            print('\nYou must enter a letter.')
            

    index = binary_search(lst, wanted)
    if index != -1:
        print(wanted, 'is at index', index)
    else:
        print(wanted, 'not in list.')