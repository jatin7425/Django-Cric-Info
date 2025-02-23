from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_email_to_client():
    subject = "this email is from django server"
    message = "this is our test message from django server"
    from_email = settings.EMAIL_HOST_USER
    recipent_list = ["vishwakarma.jatin.lits@laxmi.edu.in"]


    send_mail(subject,message,from_email,recipent_list)

def send_email_with_attachment(subject,message,recipent_list, file_path):
    mail = EmailMessage(subject=subject, body=message,from_email=settings.EMAIL_HOST_USER,to=recipent_list,)
    mail.attach_file(file_path),
    mail.send()