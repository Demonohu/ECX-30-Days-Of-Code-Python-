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
    sentence_punctuations = {}
    sentence_list = list(sentence)
    for index, letter in enumerate(sentence):
        if index<len(sentence)-1 and  letter in punctuations and sentence[index+1] == ' ':
            sentence_punctuations[index] = letter
        if letter in punctuations and index == len(sentence)-1:
            sentence_punctuations[index] = letter
    for mark_no in sentence_punctuations:
        sentence_list[mark_no] = ''
    sentence_list = ''.join(sentence_list).split()

    reversed_list = sentence_list[::-1]
    print(reversed_list)
    # print(sentence_list)
    # for mark in punctuations:

        # if sentence.index(mark) == ' ' or sentence.index(mark)==len(sentence):
            # sentence = sentence.replace(mark, '') 
    # print(sentence)
    # for word in sentence_list:
    #     for i in word:
    #         if i in punctuations and word.index(i)==(len(word)-1):
    #             word.replace(i, '')
    #             # sentence_list[-len(sentence_list[:sentence_list.index(word)+1])]+i
    #             print(i, word.index(i), sentence_list.index(word), sentence_list[:sentence_list.index(word)+1],len(sentence_list[:sentence_list.index(word)+1]) )

    # print(sentence_list)
                # print(sentence[sentence_list.index(word):])
                # print(len(sentence[sentence_list.index(word):]))
                # print(i)
                # print(sentence_list.index(word))
        
    # for idx, c in enumerate(sentence):
    #     if idx < len(sentence)-1 and c in punctuations and sentence[idx+1] == ' ':
    #         sentence_punctuations += c
    #     elif c in punctuations and (idx == len(sentence)-1):
    #         sentence_punctuations += c
    
    # sentence_punctuations_reversed = list(reversed(sentence_punctuations))
    # sentence_list = sentence.split()
    
    # reversed_sentence = ' '.join(list(reversed(sentence_list)))
    # # for idx, item in enumerate(reversed_sentence):
    # #     for i in sentence_punctuations_reversed:
    # #         if item in sentence_punctuations and (reversed_sentence[idx+1] == ' ' or (idx == len(reversed_sentence))):
    # #             item = i
    # rev_list = list(reversed_sentence.strip())
    # print(rev_list)
    # for item in rev_list:
    #     for mark in sentence_punctuations:
    #         for i in sentence_punctuations_reversed:
    #             if item == mark:
    #                 rev_list[rev_list.index(item)] = i
                    
    # print(list(reversed_sentence.strip()))
    # print(sentence_punctuations)
    # print(sentence_list)
    # print((reversed_sentence))
    # print(rev_list)

if __name__ == '__main__':
    sentence = input('Enter a sentence to reverse: ')
    reverser(sentence)



