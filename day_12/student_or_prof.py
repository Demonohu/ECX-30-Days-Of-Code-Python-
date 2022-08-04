#Student or professor.
#At a certain school, student email addresses end with
#@student.college.edu, while professor email addresses
#end with @prof.college.edu. Write a program that first
#asks the user how many email addresses they will be 
#entering, and then has the user enter those addresses.
#After all the email addresses are entered, the program
#should print out a message indicating exactly how many
#student and professor emails were entered.


def school_mails():
    no_of_mails = int(input('How many email addresses will you input? '))
    email_addys = []
    print('Enter the email addresses')
    for i in range(1, no_of_mails+1):
        while True:
            addy = input(str(i)+') ')
            if addy[-17:] == '@prof.college.edu' or addy[-20:] == '@student.college.edu':
                email_addys.append(addy)
                break
            else:
                print("\nA valid email address ends with '@student.college.edu' or '@prof.college.edu'.")
                print('Enter a valid email address.')
                continue
        

    students = 0
    profs = 0
    for email_addy in email_addys:
        if email_addy[-20:] == '@student.college.edu':
            students += 1
        else:
            profs += 1

    return students, profs

students, profs = school_mails()
print('You entered the details of', students, 'students,', profs, 'professors.')
