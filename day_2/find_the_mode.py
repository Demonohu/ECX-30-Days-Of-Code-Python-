#Find the mode
#Extend the function from day 1, to also print out the modal element(s)
#of the input list. i.e, to determine which element occurs the most.
#If there are multiple such elements, then return a list containing them all


lst = (input('Enter a list of items. \nEach item should be separated with a comma! e.g(5, 4, girl) \n: ')).split(', ')
#This takes a list of items separated with a comma and space

def list_to_set(lst):
    
    lst_set = [] #An empty list to take in the new list with no repetitions.

    for item in lst:
        if item not in lst_set:
            lst_set.append(item)

    #Check each item in the inputted list and add it to the new list 
    # if it's not already there.
    print('Here is your list without any item repeated:\n', lst_set)

def get_mode(list_of_items):
    """
   Takes in a list of items and return the mode. 
    """

    dict_of_counts = {} #Create an  empty dictionary to store counts.
    list_of_counts = [] #Create an  empty list to store counts.

    for item in list_of_items:
        item_count = list_of_items.count(item) #Count items for each item in the list
        list_of_counts.append(item_count) #Add count to the list
        dict_of_counts[item] = item_count #Add count and item in dict
    max_count = max(list_of_counts) #Get the max count of items
    if max_count == 1:
        print('This list has no mode.')
    else:
        mode_list = [] #Create an empty list to add the modes if more than 1
        for key, item in dict_of_counts.items():
            if item == max_count: #Get item from original list with most counts
                mode_list.append(str(key))
        print('The mode : ', mode_list)


list_to_set(lst)
get_mode(lst)