import requests

class Report:

    def __init__(self,token,budget_id,category_id):
        """init"""
        self.token=token
        self.budget_id=budget_id
        self.category_id=category_id
        self.column_spacing=10
        self.first_column_spacing=30

    def add_group_to_report(self,group):
        report_string=''
        for row in group['categories']:
            budgeted = row['budgeted']
            activity = row['activity']
            if (budgeted > 0 and activity < 0):

                # variables
                budgeted = budgeted / 1000
                balance = row['balance'] / 1000
                name = row['name']

                # print the report_string
                d = list([str(name).ljust(self.first_column_spacing),budgeted,balance])
                report_string += '| '.join(str(x).ljust(self.column_spacing) for x in d)+'\n'

        return report_string

    def build_report_string(self):

        url = f'https://api.youneedabudget.com/v1/budgets/{self.budget_id}/categories'

        headers={
            'Authorization': f'Bearer {self.token}' 
        }

        resp = requests.get(url=url, headers=headers)
        data = resp.json() 

        columns = [str('category').ljust(self.first_column_spacing), 'budgeted', 'balance']
        report_string = '| '.join(str(x).ljust(self.column_spacing) for x in columns)+'\n'
        report_string += ('-' * len(report_string)+'\n')

        groups = data['data']['category_groups']

        for group in groups:
            if self.category_id is None:
                report_string += self.add_group_to_report(group)
            elif group['id'] == self.category_id:
                report_string += self.add_group_to_report(group)       
            
        return report_string
