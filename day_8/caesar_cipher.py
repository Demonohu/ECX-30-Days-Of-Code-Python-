#Caeser Cipher
#A Caeser cipher is an ancient form of encryption. It involved
#taking a text(a string) as input, and encoding it by replacing
#each letter by the one n-steps next to it in the alphabet. 
#(e.g; Shifting 'Python' by 5, becomes 'Udymts'. -Note that 
#this 'shift', wraps around, which is why 'y' becomes 'd'.).
#Task:
#*Write a function that takes in as parameters, a plaintext(string)
#to encode, and a_shift value_, and outputs the encoded value of 
#the string.
#*Write another similar function that takes in the encoded string, 
#with a shift_value, and decodes it.
#*Finally, write a third function that takes in a text, a shift 
#value, and a third parameter to indicate whether to encode or
#decode the given text.(i.e f('String', 5, True/False)), and 
#print out the encoded(or decoded) text accordingly.


import string

text = input('Enter a text to encode or decode: ')
while True:
    try:
        shift_value = int(input('Enter the shift value to code with: '))
        break
    except ValueError:
        print('Enter the number not the number in letters!')
        continue

while True:
    what_code = input('Decode or encode? ')
    if what_code.lower() == 'decode' or what_code.lower() == 'encode':
        break
    else:
        print('Wrong input.')
        continue

def encoder(plaintext, shift_value):
    alphabets = string.ascii_lowercase
    encoded = []
    for letter in plaintext.lower():
        alphabet_position = alphabets.find(letter)
        encoding_position = alphabet_position + shift_value
        encoded.append(alphabets[(encoding_position%26)])
    return ''.join(encoded)


def decoder(coded_text, shift_value):
    alphabets = string.ascii_lowercase
    decoded_text = []
    for letter in coded_text.lower():
        alphabet_position = alphabets.find(letter)
        decoding_position = alphabet_position - shift_value
        decoded_text.append(alphabets[decoding_position%26])
    return ''.join(decoded_text)


def xcode(text, shift_value, what_code):
    if what_code.lower() == 'encode':
        return encoder(text, shift_value)
    else:
        return decoder(text, shift_value)

print(xcode(text, shift_value, what_code))
