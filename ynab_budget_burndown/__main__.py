import os
import settings
from report import Report
from dispatcher import Dispatcher

BEARER_TOKEN=os.getenv("BEARER_TOKEN")
BUDGET_ID=os.getenv("BUDGET_ID")
CATEGORY_ID=os.getenv("CATEGORY_ID")

SENDER_EMAIL_ID=os.getenv("SENDER_EMAIL_ID")
SENDER_EMAIL_PASSWORD=os.getenv("SENDER_EMAIL_PASSWORD")
RECIPIENTS=os.getenv("RECIPIENTS")

def main():
    report = Report(BEARER_TOKEN,BUDGET_ID,CATEGORY_ID)
    print('Building report...')
    message = report.build_report_string()

    dispatcher = Dispatcher(SENDER_EMAIL_ID,SENDER_EMAIL_PASSWORD,RECIPIENTS)
    print('Sending report...')
    dispatcher.email("Disposable Income Report", message)
    print('Report sent to '+RECIPIENTS)

if  __name__ =='__main__':main()