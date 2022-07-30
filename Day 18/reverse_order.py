#Reverse order.
#Write a function that takes a string as input, and
#returns a string similar to the input, but with the
#words  in reverse order, and the punctuation marks 
#maintaining their original order.
#e.g;
#f("Hello. I'm Edwin A.J, and you?") => "You and. A.J Edwin I'm, Hello?"
#f("What time is it? Hammer time.") => "Time Hammer? It is time what."
#Note: As shown in the example above, the order of the punctuation marks('?', ',', '.') have not changed.
#Only the words have.


import string

def reverser(sentence):
    punctuations = string.punctuation
    sentence_punctuations = []
    for idx, c in enumerate(sentence):
        if idx < len(sentence)-1 and c in punctuations and sentence[idx+1] == ' ':
            sentence_punctuations += c
        elif c in punctuations and (idx == len(sentence)-1):
            sentence_punctuations += c
    
    sentence_punctuations_reversed = list(reversed(sentence_punctuations))
    sentence_list = sentence.split()
    
    reversed_sentence = ' '.join(list(reversed(sentence_list)))
    # for idx, item in enumerate(reversed_sentence):
    #     for i in sentence_punctuations_reversed:
    #         if item in sentence_punctuations and (reversed_sentence[idx+1] == ' ' or (idx == len(reversed_sentence))):
    #             item = i
    for item in sentence_list:
        for mark in sentence_punctuations:
            for i in sentence_punctuations_reversed:
                if mark in item:
                    sentence_list.replace(mark, i)
    # print(sentence_punctuations)
    print(sentence_list)
    print((reversed_sentence))

if __name__ == '__main__':
    sentence = input('Enter a sentence to reverse: ')
    reverser(sentence)



