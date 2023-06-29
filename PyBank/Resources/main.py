import os
import csv

csvpath = os.path.join('python-challenge', 'PyBank/Resources', 'budget_data.csv')

total_months = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
