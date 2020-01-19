import requests
import os
import settings


BUDGET_ID=os.getenv('BUDGET_ID')
BEARER_TOKEN=os.getenv('BEARER_TOKEN')
CATEGORY_ID=os.getenv('CATEGORY_ID')


class Report:
    

    def __init__(self):
        """Initialization"""

    def load_bugdet_categories(self):
        url = f'https://api.youneedabudget.com/v1/budgets/{BUDGET_ID}/categories'

        headers={
            'Authorization': f'Bearer {BEARER_TOKEN}' 
        }

        resp = requests.get(url=url, headers=headers)
        self.data = resp.json()

    def get_group(self):
        groups = self.data['data']['category_groups']

        for group in groups:
            if group['id'] == CATEGORY_ID:
                break
        else:
            group = None

        self.group=group

    def print_report(self):
        dash = '-' * 75

        text = dash+'\n'
        text += '{:<40s}{:<10s}{:<10s}{:>10s}'.format('category','budgeted','balance','percent used')+'\n'
        text += dash+'\n'

        for item in self.group['categories']:
            budgeted = item['budgeted']
            balance = item['balance']
            name = item['name']
            if budgeted > 0:
                leftover = budgeted - balance
                fractionLeftover = leftover / budgeted
                percentUsed = fractionLeftover * 100
                text += '{:<40s}${:<10.2f}${:<10.2f}{:>10.1f}%'.format(name,budgeted/1000,balance/1000,percentUsed)+'\n'

        return text
