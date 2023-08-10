from email.message import EmailMessage 
import ssl
import smtplib


email_sender = "YOUREMAIL@gmail.com"

email_password = "YOUR_PASSWER"

email_reciever = "yovitem847@dotvilla.com"

subject = "Test"

body = "hiiii"
em = EmailMessage()

em["From"]=email_sender
em["To"]=email_reciever
em["Subject"]=subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())

