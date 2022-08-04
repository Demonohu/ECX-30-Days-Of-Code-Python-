# Frequency analysis
#1) Write a function that takes a string as input and:
#Returns a dictionary whose keys are the characters 
#found in the text, and whose values are the number 
#of occurrences of that character in the text.
#e.g; f("It is good!") => 
#{'I': 2, 't':1, 's':1, 'g':1, 'o':2, 'd':1, '!':1}

#2) Write another function that takes an input string
#and returns a dictionary whose keys are the words in
#the text, and whose values are the respective frequencies
#of these words. e.g; f('It is not good, is it?') => 
#{'It':2, 'is':2, 'not':1, 'good':1}
#Note: In both cases, disregard case sensitivity.


import string

def frequency_1(sentence):
    frequency_dict = {}
    sentence = sentence.replace(' ', '').lower()
    for i, j in enumerate(sentence):
        freq = 1
        for k in sentence[:i]+sentence[i+1:]:
            if j == k:
                freq += 1
        frequency_dict[j] = freq
    print(frequency_dict)



def frequency_2(sentence):
    frequency_dict = {}
    punctuations = string.punctuation
    for idx, c in enumerate(sentence):
        if idx < len(sentence)-1 and c in punctuations and sentence[idx+1] != ' ':
            sentence = sentence.replace(c, '')
    sentence = sentence.lower()
    sentence = ''.join(sentence).split()
    for i, j in enumerate(sentence):
        freq = 1
        for k in sentence[:i]+sentence[i+1:]:
            if j == k:
                freq +=1
        frequency_dict[j] = freq
    print(frequency_dict)
    


if __name__ == '__main__':
    sentence = input('Enter a sentence: ')
    frequency_1(sentence)
    frequency_2(sentence)