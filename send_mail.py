import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailSender:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(sender, password)

    def send_mail(self, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        self.server.sendmail(self.sender, recipient, text)
        # self.server.quit()

# Example usage:
sender_email = 'comon928@gmail.com'
sender_password = 'knscyyvmxmaalyfp'

mail_sender = MailSender(sender_email, sender_password)

