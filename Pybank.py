#Challenge 3 

#Import files
import os
import csv

#pybank 

#Load in pybank dataset           
file_path = os.path.join('resources','budget_data.csv')


 
with open(file_path) as budgetcsv:
    
    budgetdata = csv.reader(budgetcsv, delimiter = ',')
    
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
#Monhts and total loop
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

        
    
    avgmonthlydiff = totalmonthlydiff/ (months - 1)
    
#pybank answers:
print('financial analysis')
print("-------------------------")
print(f"Total Months: {months}")
print(f"Total $ amount: ${total}")
print(f"Average Chage: ${avgmonthlydiff}")
print(f"Greatest Increase in profits :({dateofmax}) ${maxdiff}")
print(f"Greatest Decrease in profits : ({dateofmin}) ${mindiff}")

