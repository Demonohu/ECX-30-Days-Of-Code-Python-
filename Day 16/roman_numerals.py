#When in Rome
#*Write a function that takes an integer as input, 
#and returns it's translation to Roman numerals.
#*Using the aforementioned function, write a program
#that takes user input and prints out their Roman 
#numeral form. This program must include all necessary
#type checks or Exception handling.



def arabic_to_roman(arabic, roman_numeral_chart):
    if arabic in roman_numeral_chart:
        roman_numeral = roman_numeral_chart[arabic]
        return roman_numeral
    else:
        if 10 > arabic < 100:
            unit = arabic%10; tens = (arabic % 100) - unit
            roman_numeral = ''
            roman_numeral = ''
        unit = arabic%10; tens = (arabic % 100) - unit;  hundreds = (arabic % 1000) - (tens + unit); 
        thousands = (arabic % 10000) - (hundreds + tens + unit)
        roman_numeral = ''
        roman_numeral += roman_numeral_chart[thousands] + roman_numeral_chart[hundreds] + roman_numeral_chart[tens] + roman_numeral_chart[unit] 
        print(roman_numeral)


def roman_to_arabic(roman, arabic_numeral_chart):
    if roman in arabic_numeral_chart:
        arabic = arabic_numeral_chart[roman]
        return arabic

    else:
        arabic = 0
        n = len(roman)
        for (idx, c) in enumerate(roman):
            if idx < n-1 and arabic_numeral_chart[c] < arabic_numeral_chart[roman[idx+1]]:
                arabic -= arabic_numeral_chart[c]
            else:
                arabic += arabic_numeral_chart[c]
        
        print(arabic)


if __name__ == "__main__":
    roman_numeral_chart= {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X',
                     20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC', 100:'C', 
                     200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM', 
                     1000:'M', 2000:'MM', 3000:'MMM'}
    arabic_numeral_chart = {value: key for key, value in roman_numeral_chart.items()}

    print('Do you want to convert to or from roman numerals? ')
    isValid = True
    while isValid:
        work = input("'to' for Arabic to Roman, 'from' for Roman from Arabic: ")
        if work.lower() == 'to' or work.lower()== 'from':
            break
        else:
            print('\nEnter a valid selection')
            continue
    
    
    if work == 'to':
        while isValid:
            try:
                arabic = int(input('Enter the arabic number to be converted. Number should be greater than 0 and less than 4000: '))
                if int(arabic) >= 1 and int(arabic) <= 3999:
                    break
                else:
                    print('\n Enter a valid integer.')
                    continue
            except ValueError:
                print('\n Enter a valid integer.')
                continue
        arabic_to_roman(arabic, roman_numeral_chart)

    else:
        while isValid:
            roman = (input('Enter the roman numeral to be converted: ')).upper()
            roman_letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
            if roman.isalpha():
                if all([char in 'IVXLCDM' for char in roman]):
                    break
                else:
                    print('\n Enter a valid roman numeral.')
                    continue
        roman_to_arabic(roman, arabic_numeral_chart)


