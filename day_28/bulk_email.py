#Bulk E-mail.
#Using the built-in SMTP module, write a function
#that takes a list of emails as input, and sends 
#each of them an(any) email message.


import smtplib, ssl, re
from email.message import EmailMessage


def bulk_mail(receivers, email_sender, email_password, subject, body):

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = receivers
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for addy in receivers:
            smtp.sendmail(email_sender, addy, em.as_string())
        print('Successfully sent mails.')
    

if __name__ == '__main__':
    no_of_receivers = input('How many people do you want to send mails to?\nFigures only: ')

    receivers = []
    mail_format = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    print('\nEnter the email addresses.')

    for i in range(1, int(no_of_receivers)+1):
        isValid = False #Set to false again so it can be used to validate the other inputs.
        while not isValid:
            receiver = input(str(i)+') ')
            if re.match(mail_format, receiver):
                receivers.append(receiver)
                isValid = True
            else: 
                print()
                print('Enter a valid email address')

    print()
    subject = input("Enter the subject of the mail:\n")
    print()
    body = input("""Enter the body of the mail:\n""")

    isValid = False
    while not isValid:
        print()
        email_sender = input('Enter the email address of the sender: ')
        if re.match(mail_format, email_sender):
            isValid = True
        else: 
            print()
            print('Enter a valid email address')

    passwordValid = False
    while not passwordValid:
        print()
        email_password = input("Enter the password for the mail.\nIf it's a gmail, generate a password for third party apps. ")
        try:
            bulk_mail(receivers, email_sender, email_password, subject, body)
            passwordValid = True

        except smtplib.SMTPAuthenticationError:
            print('Incorrect password.')      