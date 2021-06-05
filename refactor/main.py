from email_class import Email
from settings import login, password

if __name__ == '__main__':
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None
    email = Email(login, password)
    email.send_email(subject, recipients, message)
    email.recieve_email(header)
