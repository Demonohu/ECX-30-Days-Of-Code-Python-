#Write a function that takes in a date as input, and returns 
#what day of the week it is. 
#*The input date can be in any convenient format
#(Whether a 'ddmmyy' string, a series of integers, etc)
# *Your function must work for both future and past dates.
# *Exception handling (or Type checking) is necessary.


import datetime
import calendar

def day_of_the_week(day, month, year):
    the_date = datetime.datetime.strptime((day+ month+ year), '%d%m%Y').weekday()
    week_day = calendar.day_name[the_date]
    print(week_day)

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
            isValid = True

        except ValueError:
            print('Date provided does not exist.\n')