

#Import files
import os
import csv

#Load in pybank dataset           
file_path = os.path.join('pybank','resources','budget_data.csv')

 
with open(file_path) as budgetcsv:
    
    budgetdata = csv.reader(budgetcsv, delimiter = ',')

#Set variables going into Dataset
    header = next(budgetdata)


    months = 1
    monthly_diff = 0
    previousmonth = float(next(budgetdata)[1])
    total = previousmonth
    totalmonthlydiff = 0
    previousmonthlydiff = 0
    maxdiff = 0
    mindiff = 0
    dateofmax = []
    dateofmin = []

#For Loop
    for rows in budgetdata:
        months+= 1
        currentmonth = float(rows[1])
        total += currentmonth
        monthly_diff = currentmonth - previousmonth
        previousmonth = currentmonth
        if monthly_diff > maxdiff:
           maxdiff = monthly_diff
           dateofmax = rows[0]

        elif monthly_diff < mindiff:
            mindiff = monthly_diff
            dateofmin = rows[0]

        totalmonthlydiff  += monthly_diff
        previousmonthlydiff = monthly_diff

#Calculate results after for loop
    
    avgmonthlydiff = totalmonthlydiff/ (months - 1)
    
#pybank answers:
print('financial analysis')
print("-------------------------")
print(f"Total Months: {months}")
print(f"Total $ amount: ${total}")
print(f"Average Chage: ${avgmonthlydiff}")
print(f"Greatest Increase in profits :({dateofmax}) ${maxdiff}")
print(f"Greatest Decrease in profits : ({dateofmin}) ${mindiff}")

with open("Pybank.txt", "a") as pybank:
    print('financial analysis', file = pybank)
    print("-------------------------",file=pybank)
    print(f"Total Months: {months}", file = pybank)
    print(f"Total $ amount: ${total}", file= pybank)
    print(f"Average Chage: ${avgmonthlydiff}", file = pybank)
    print(f"Greatest Increase in profits :({dateofmax}) ${maxdiff}", file= pybank)
    print(f"Greatest Decrease in profits : ({dateofmin}) ${mindiff}", file= pybank)
