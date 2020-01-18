import requests
import os

BUDGET_ID=os.getenv('BUDGET_ID')
BEARER_TOKEN=os.getenv('BEARER_TOKEN')
CATEGORY_ID=os.getenv('CATEGORY_ID')

url = f'https://api.youneedabudget.com/v1/budgets/{BUDGET_ID}/categories'

headers={
    'Authorization': f'Bearer {BEARER_TOKEN}' 
}

resp = requests.get(url=url, headers=headers)
data = resp.json() 

groups = data['data']['category_groups']

for group in groups:
    if group['id'] == CATEGORY_ID:
        break
else:
    group = None

dash = '-' * 75

print(dash)
print('{:<40s}{:<10s}{:<10s}{:>10s}'.format('category','budgeted','balance','percent used'))
print(dash)

for item in group['categories']:
    budgeted = item['budgeted']
    balance = item['balance']
    name = item['name']
    if budgeted > 0:
        leftover = budgeted - balance
        fractionLeftover = leftover / budgeted
        percentUsed = fractionLeftover * 100
        print('{:<40s}${:<10.2f}${:<10.2f}{:>10.1f}%'.format(name,budgeted/1000,balance/1000,percentUsed))