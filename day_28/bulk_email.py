#Bulk E-mail.
#Using the built-in SMTP module, write a function
#that takes a list of emails as input, and sends 
#each of them an(any) email message.


import smtplib
import ssl
from email.message import EmailMessage
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

#Enter email address list
receivers = []

def bulk_mail(receivers):
    #Enter the sender's(your) email address, password
    email_sender = ''
    email_password = ''
    email_receiver = receivers
    
    #Enter the subject of the mail.
    subject = ""

    #Enter the body of the mail
    body = """"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for addy in email_receiver:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print('Successfully sent mails.')
    
bulk_mail(receivers)