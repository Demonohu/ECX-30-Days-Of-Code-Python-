#Bubble sort.
#'Bubble sort' is a basic algorithm for sorting (rearranging
#in ascending or descending order) elements in a list. 
#It operates as follows:
#1) Iterate across a list, element by element.
#2) Upon encountering any two adjacent elements which are in
#the 'wrong' designated order(ascending or descending), swap 
#their positions in the list-else, do nothing. 
#3) Do this until your iteration reaches the end of the list
#4) Repeat steps 1 through 3 until there are no longer any
#adjacent elements in the 'wrong' order. then STOP.
#(See more at: Bubble sort.)
#Write a function that takes in two parameters, one list of
#alphabets and one flag designating what order in which to
#sort. Using the Bubble sort algorithm,
#e.g; f(['x', 'c', 'b', 'v', 'z', 'a'], descending => ['a', 'b', 'c', 'v', 'x', 'z'])
#Note: Type checking(or Exception Handling) is necessary. Disregard case-sensitivity.



def bubble_sort(lst, order):
    if order.lower() == 'descending':
        for tries in range(len(lst)):
            for ct, a in enumerate(lst):
                if (ct < len(lst)-1) and (a.lower() < lst[ct+1]):
                    lst[ct], lst[ct+1] = lst[ct+1], lst[ct]
    else:
        for tries in range(len(lst)):
            for ct, a in enumerate(lst):
                if (ct < len(lst)-1) and (a.lower() > lst[ct+1]):
                    lst[ct], lst[ct+1] = lst[ct+1], lst[ct]

    print(lst)


if __name__ == '__main__':
    isOrderValid = False
    while not isOrderValid:
        order = input('Ascending or descending order? ')
        if order.lower() == 'descending' or order.lower() == 'ascending':
            isOrderValid = True
        else:
            print('\nEnsure you enter a valid input.')

    print()
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

    bubble_sort(lst, order)
            