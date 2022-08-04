#Zodiac
#Extend the function from day 19 to return BOTH the
# day of the week AND the corresponding 'Zodiac sign' 
#of the input date. Return value can be a list or 
#ANY convenient structure. All rules relating to 
#task 19 still apply. 
#(See more on Western astrological signs.)

import datetime
import calendar
from ..day_19.DayOfTheWeek import day_of_the_week



def zodiac(day, month):
    day = int(day); month = int(month)
    zodiac_sign = ''
    if (month == 1 and day <= 19) or (month == 12 and day>= 22):
        zodiac_sign = 'Capricorn'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = 'Aquarius'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_sign = 'Pisces'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = 'Taurus'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = 'Gemini'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = 'Cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = 'Leo'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = 'Virgo'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 21):
        zodiac_sign = 'Libra'
    elif (month == 10 and day >= 22) or (month == 11 and day <= 21):
        zodiac_sign = 'Scorpio'
    else:
        zodiac_sign = 'Sagittarius'

    print(zodiac_sign)
        


if __name__ == '__main__':
    isValid = False
    while not isValid:
        try:
            print('For the date, enter the month and day in double figures; and the year in quadruple figures.')
            isDayValid = False
            while not isDayValid:
                day = input('Enter the day: ')
                if day.isdigit() and len(day)==2 and 1<=int(day)<=31:
                    isDayValid = True
                else:
                    print("Input is invalid.\nDay must be two figures long and between 1 and 31.\n")

            isMonthValid = False
            while not isMonthValid:    
                month = input('\nEnter the month: ')
                if month.isdigit and len(month)==2 and 1<=int(month)<=12:
                    isMonthValid = True
                else:
                    print('Input is invalid.\nMonth must be two figures long and betwwen 1 and 12.\n')

            isYearValid = False
            while not isYearValid:
                year = input('\nEnter the year: ')
                if year.isdigit() and len(year)==4:
                    isYearValid = True
                else:
                    print('Input is invalid.\nYear must be four figures long.')

            day_of_the_week(day, month, year)
            zodiac(day, month)
            isValid = True

        except ValueError:
            print('Date provided does not exist.\n')