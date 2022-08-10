#GPA Calculator.
#Write a function that:
#1) Takes as parameters, a list of tuples, containing grades and their corresponding units. 
#(e.g; [('A', 2), ('A', 3), ('B', 2), ...etc])
#2) Computes and returns the student GPA, based on the values provided.
#*Note: Handle all necessary exceptions and/or edge cases.

def GPA_calculator(grades):
    grade_points = {'A':5, 'B':4, 'C':3, 'D':4, 'E':1, 'F':0}
    den=0; num = 0
    for course in grades:
        den += int(course[1])
        num += (int(course[1])*grade_points.get(course[0].upper()))
    GPA = num/den
    return round(GPA, 2)


if __name__ == '__main__':
    isValid = False
    while not isValid:
        no_of_courses = input('How many courses are you filling? ')
        if no_of_courses.isdigit():
            isValid = True
        else:
            print('Input should be figures only.')
            print()
    
    grades = []
    print('\nEnter the grade and unit seperated with a comma and no space.(e.g; B,2)')
    for course in range(1, (int(no_of_courses)+1)):
        isValid = False #Set to false again so it can be used to validate the other inputs.
        while not isValid:
            course_info = (input(str(course)+ ': ')).replace(',','')
            course_info = tuple(course_info)
            if course_info[0].isalpha() and course_info[1].isdigit():
                if 1<= int(course_info[1]) <= 3 and (course_info[0].upper() <= 'F'):
                    grades.append(course_info)
                    isValid = True
                else:
                    print()
                    print('Course unit must be between 1 and 3 and grade must be between A and F.')
                    print()
            else:
                print()
                print("Read the instructions and enter a valid input.")
                print()

    GPA = GPA_calculator(grades)
    print('Your GPA is', GPA)