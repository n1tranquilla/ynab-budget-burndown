# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
import os 
import settings
from report import Report

SENDER_EMAIL_ID=os.getenv("SENDER_EMAIL_ID")
SENDER_EMAIL_PASSWORD=os.getenv("SENDER_EMAIL_PASSWORD")
RECIPIENTS=os.getenv("RECIPIENTS")

class Dispatcher:

    def __init__(self):
        """Initialization"""
        self.report = Report()
        self.report.load_bugdet_categories()
        self.report.get_group()

    def dispatch(self):
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        # start TLS for security 
        s.starttls() 

        # Authentication 
        s.login(SENDER_EMAIL_ID, SENDER_EMAIL_PASSWORD) 

        # message to be sent 
        message = self.report.print_report()

        # sending the mail 
        s.sendmail(SENDER_EMAIL_ID, RECIPIENTS, message) 

        # terminating the session 
        s.quit() 
