from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib

load_dotenv()
import os



def send_tasks_to_your_email(email_sender, email_password, email_receiver, tasks_content):
    
    subject = 'Your To do list'
    body =  f"These are the tasks you set to do:\n\n{tasks_content}\nHave a nice day! 😃"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)




    email_receiver= os.getenv('EMAIL_RECIEVER')
    subject= 'YOUR TASKS'
    context = ssl.create_default_context()
 
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
     smtp.login(email_sender,email_password)
     smtp.sendmail(email_sender,email_receiver,em.as_string())