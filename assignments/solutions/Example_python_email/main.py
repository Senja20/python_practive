import smtplib  # main library to work with smtp-protocol
import imghdr  # used for sending images
from email.message import EmailMessage  # importing a class for email set up

EMAIL_ADDRESS = 'yauheny@uia.no'
EMAIL_PASSWORD = 'DigitalFortress2000'

contacts = ['yauhen.yavorski@gmail.com', 'yauheny@uia.no']

msg = EmailMessage()
msg['Subject'] = 'Python test'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Test program\u2764\ufe0f.'
                '\nHere is a picture and out assignment 9:')

with open('send-emails-gmail-python.jpg', 'rb') as file:
    file_data = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with open('Assignment 9 - IKT-104.pdf', 'rb') as pdf_file:
    file_data = pdf_file.read()
    file_name = pdf_file.name

msg.add_attachment(file_data, maintype='assignment', subtype='octet-string', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
    smtp.quit()


    # Can also use, but it is more primitive way:
    # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #    smtp.ehlo()  # identifies with mail server
    #    smtp.starttls()  # inception
    #    smtp.ehlo()

    # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # subject = 'Python test'
    # body = 'This is a test e-mail using Python'
    # msg = f'Subject: {subject}\n\n{body}'
    # smtp.sendmail('yauhen.yavorski@gmail.com', 'yauhen.yavorski@gmail.com', msg)

    # smtp.send_message(msg)
