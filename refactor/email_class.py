import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, login, password):
        self.smtp = "smtp.gmail.com"
        self.imap = "imap.gmail.com"
        self.login = login
        self.password = password

    def login(self, protocol):
        if protocol == 'send':
            ms = smtplib.SMTP(self.smtp, 587)
            # identify ourselves to smtp gmail client
            ms.ehlo()
            # secure our email with tls encryption
            ms.starttls()
            # re-identify ourselves as an encrypted connection
            ms.ehlo()
            ms.login(self.login, self.password)
        else:
            ms = imaplib.IMAP4_SSL(self.imap)
            ms.login(self.login, self.password)
        return ms

    def send_email(self, subject, recipients, message):
        ms = self.login('send')
        msg = MIMEMultipart()
        msg['From'] = self.login()
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()
        return 'Email was send'

    def recieve_email(self, header=None):
        ms = self.login
        ms.list()
        ms.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = ms.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = ms.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = ms.message_from_string(raw_email)
        ms.logout()
        return email_message
