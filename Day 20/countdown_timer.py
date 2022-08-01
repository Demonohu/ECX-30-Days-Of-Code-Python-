#Countdown Timer.
#Write a program that:
#1) Asks the user to enter a time period in the form of a 
#nuumber with a unit of either seconds, minutes, or hours. 
#(e.g; '44s','32m', '10h'.). The last character of the string 
#entered would be used to determine its unit.
#2) Counts down from the input value, and prints out the time 
#left on the clock every second.
#3) When the time is exhausted, makes a beeping sound non-stop 
#until the user exits the app.
#For example: T>Enter a time
#User> 5s
#T> 5 seconds left
#>4 seconds left
#>3 seconds left
#>2 seconds left
#>1 second left
#*continous indefinite beeping*
#(Hint: A 'beeping sound'  can be achieved using the 'bell character',
#or any library of your choice.


def countdown(t):
    time_unit = t[-1:]
    if time_unit.lower() == 's':
        time_no = int(t[:-1])
    elif time_unit.lower() == 'm':
        time_no = (int(t[:1]))*60
    else:
        time_no = (int(t[:1]))*3600
    
    for i in range(time_no, 0, - 1):
        if i > 1:
            print(i, 'seconds left.')
        else:
            print('1 second left.')


        
if __name__ == '__main__':
    isValid = True
    while isValid:
        print('Time entered should have unit.(s/m/h) e.g; 5m/7h/9s')
        time_given = input('Enter the time to be counted down: ')
        if time_given[-1:].lower() == 'm' or time_given[-1:].lower() == 'h' or time_given[-1:].lower() == 's':
            try:
                countdown(time_given)
                break
            except Exception:
                print('Something is wrong')
                again = input('Do you want to try again?(yes/no)')
                if again.lower == 'yes' or again.lower() == 'y':
                    break
                else:
                    print()
                    continue
            
        else:
            print()
            continue