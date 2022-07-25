# What's the acronym(s)?
# Ask the user to enter a sentence with an acronym or more,and
# you'll return--and--print all the acronyms in the sentence. 
# Input -> "I need to get this done ASAP." Output -> "ASAP"
# Input -> "SMH. The NPF is really a joke." Output -> "SMH NPF"
# Input -> "LOOOL. I thought you were at KFC." Output -> "LOOOL KFC"
# (Note : An "acronym", for our purposes, is defined as any continuous sequence of uppercase letters.)


def acronyms_finder():
    sentence = input('Enter a sentence: ')
    if ',' in sentence:
        sentence = sentence.replace(',','')
    elif '.' in sentence:
        sentence = sentence.replace('.','')
    sentence = list(sentence.split(" "))
    acronyms = ""
    for word in sentence:
        if len(word) > 1 and word.isupper():
            acronyms +=  word + " "
    
    if acronyms != "":
        return acronyms

    else:
        return "No acronyms in the sentence you gave."

print(acronyms_finder())
