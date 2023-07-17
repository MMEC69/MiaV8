#testing email sending
#Successed -> YES
import os
from email.message import EmailMessage
import ssl
import smtplib

#email_sender = 'coorayeronnemanoshawoodapple@gmail.com'

email_sender = input("give me the username (with user@sample.com): ")

#email_password = 'fljihrfefmydrskc'

email_password = input("give me the password: ") #give your custome password for app created from your account

#email_receiver = 'coorayeronnemanoshapineapple@gmail.com'

email_receiver = input("give me receiver (with user@sample.com): ")

#subject = "subject title"

subject = input("state the subject: ")

#body = "info mation regarding email"

body = input("give the message: ")

em = EmailMessage()

em['From'] = email_sender

em['To'] = email_receiver

em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


