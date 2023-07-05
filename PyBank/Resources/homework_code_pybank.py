import os
import csv

csvpath = os.path.join('..','python-challenge', 'PyBank/Resources', 'budget_data.csv')

total_profit_losses = int(0)
total_months = int(0)
sum_profit_losses = int(0)
greatest_increase = int(0)
greatest_decrease = int(99999999999999)

greatest_increase_month = ""
greatest_decrease_month = ""


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        profit_losses = int(row[1])
        total_profit_losses += int(profit_losses)
    
        total_months = total_months + 1

        if total_months > 1:
            change = profit_losses - last_profit_losses

            sum_profit_losses = sum_profit_losses + change

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
                
            
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        last_profit_losses = int(row[1])
        
print('Financial Analysis')
print('------------------------')
print("Total months:", total_months)

#Syntax for printing in currency format ('${:,.2f}'.format) was accessed on online in a Python forum.
print("Total:", '${:,.2f}'.format(total_profit_losses))

#There is no change on the first month, so average change calculation uses total_months - 1.
print("Average Change:", '${:,.2f}'.format(sum_profit_losses / (total_months -1), 2))
print("Greatest Increase in Profits:", greatest_increase_month, '${:,.2f}'.format(greatest_increase))
print("Greatest Decrease in Profits:", greatest_decrease_month, '${:,.2f}'.format(greatest_decrease))

#Reference text file with the intention of writing to it.
pybank_output = open("pybank_ouput.txt", "w")

pybank_output.write('Financial Analysis')
pybank_output.write('\n------------------------')
pybank_output.write('\n Total months:')
pybank_output.write(f'{total_months}')
pybank_output.write('\nTotal:')
pybank_output.write('${:,.2f}'.format(total_profit_losses))
pybank_output.write('\nAverage Change:')
pybank_output.write('${:,.2f}'.format(sum_profit_losses / (total_months -1), 2))
pybank_output.write('\nGreatest Increase in Profits:')
pybank_output.write(greatest_increase_month,)
pybank_output.write('  ')
pybank_output.write('${:,.2f}'.format(greatest_increase))
pybank_output.write("\nGreatest Decrease in Profits:")
pybank_output.write(greatest_decrease_month,)
pybank_output.write('  ')
pybank_output.write('${:,.2f}'.format(greatest_decrease))
pybank_output.close()

