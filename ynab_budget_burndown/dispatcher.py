import smtplib
from email.mime.text import MIMEText

class Dispatcher:

    def __init__(self,sender_email,sender_password,recipients):
        self.sender_email=sender_email
        self.sender_password=sender_password
        self.recipients=recipients

    def email(self,subject,message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = self.recipients

        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        # start TLS for security 
        s.starttls() 

        # Authentication 
        s.login(self.sender_email, self.sender_password) 

        # sending the mail 
        s.sendmail(self.sender_email, self.recipients, msg.as_string()) 

        # terminating the session 
        s.quit() 

