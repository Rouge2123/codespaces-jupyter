### Lists
list = [1, 4, 6, 2, 5, 9, 4, 7, 9]

## find max and min of a list
x = 0

## remove duplicates

### Speed problem
finTrans = [{"typePS": "P", "amount": 100, "date": "160124"}, 
            {"typePS": "S", "amount": 93, "date": "160124"}, 
            {"typePS": "P", "amount": 12, "date": "160124"}, 
            {"typePS": "S", "amount": 45, "date": "160124"}, 
            {"typePS": "S", "amount": 82, "date": "160124"}]

def amountOfTrans(date):
    length = 0
    for i in finTrans:
        if i["date"] == date:
            length += 1
    print(length)

amountOfTrans("160124")

def totalIncomeAndExpense():
    income = 0
    expense = 0
    for i in finTrans:
        if i["typePS"] == "P":
            expense += i["amount"]
        elif i["typePS"] == "S":
            income += i["amount"]
    print(f"Total income: {income}, total expense: {expense}")
totalIncomeAndExpense()

# Using list comprehension
def list_of(my_key):
    amount_values = [transaction[my_key] for transaction in finTrans]
    return amount_values
print(list_of("amount"))

def sum_up(my_type):
    amonut_values = [transaction['amount'] for transaction in finTrans]
    # if transaction['typePS'] == my_type:
    #     return (sum(amonut_values))
    
def find_all(my_key,my_type):
    total = [tran[my_key] for tran in finTrans if tran['date'] == my_type]
    return total
print(find_all('date','160124'))

import re

def is_valid_date_format(date_string):
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    #this doesn't check for month/day order
    return bool(date_pattern.match(date_string))

import numpy as np
import pandas as pd

a = [[1,2],[3,4]]
c = [[10,100]]

A = np.array(a)
C = np.array(c)
print(A.shape)
print(C.shape)

a * c 