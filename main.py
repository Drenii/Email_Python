from email.message import EmailMessage
import ssl, smtplib
from pw import password


email_sender='dreni107@gmail.com'
email_password=password

email_receiver='dreni107@hotmail.com'

subject="Hello, Can you read this email again please"
body="""
when you read this email don't forget to reply!"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())

