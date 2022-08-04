"""
List to set
Create a function that takes in a list as input. and returns(and prints)
a new list with all repetitions reduced to one appearance alone, as output,
e.g; f(['a', ' b', 'a', 'a', 3, 3, 2, 'hello', 'b']) 
=> ['a', 'b', 3, 2, 'hello']. output
"""


def list_to_set():

    lst = (input('Enter a list of items. \nEach item should be separated with a comma! e.g(5, 4, girl) \n: ')).split(', ')
    #This takes a list of items separated with a comma and space
    
    lst_set = [] #An empty list to take in the new list with no repetitions.

    for item in lst:
        if item not in lst_set:
            lst_set.append(item)
    #Check each item in the inputted list and add it to the new list 
    # if it's not already there.
    print(lst_set)

list_to_set()

def list_to_set2():

    lst = (input('Enter a list of items. \nEach item should be separated with a comma! e.g(5, 4, girl) \n: ')).split(', ')
    #This takes a list of items separated with a comma and space

    lst_set = set(lst) 
    #Creates a list of the inputted list without repeating any item
    print(lst_set)

list_to_set2()