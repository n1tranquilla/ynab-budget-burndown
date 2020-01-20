import requests

class Report:

    def __init__(self,token,budget_id,category_id):
        """init"""
        self.token=token
        self.budget_id=budget_id
        self.category_id=category_id

    def build_report_string(self):

        url = f'https://api.youneedabudget.com/v1/budgets/{self.budget_id}/categories'

        headers={
            'Authorization': f'Bearer {self.token}' 
        }

        resp = requests.get(url=url, headers=headers)
        data = resp.json() 

        groups = data['data']['category_groups']

        for group in groups:
            if group['id'] == self.category_id:
                break
        else:
            group = None


        columns = ['category', 'budgeted', 'balance', 'percent used']
        report_string = '|'.join(str(x).ljust(30) for x in columns)+'\n'
        report_string += ('-' * len(report_string)+'\n')

        for row in group['categories']:
            budgeted = row['budgeted']
            activity = row['activity']
            print(activity)
            if (budgeted > 0 and activity < 0):

                # variables
                budgeted = budgeted / 1000
                balance = row['balance'] / 1000
                name = row['name'] 
                leftover = budgeted - balance
                fractionLeftover = leftover / budgeted
                percentUsed = fractionLeftover * 100

                # print the report_string
                d = list([name,budgeted,balance,percentUsed])
                report_string += '|'.join(str(x).ljust(30) for x in d)+'\n'

        return report_string
