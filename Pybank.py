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
    #max_change = 0
    #min_change = 0
    
#Monhts and total loop
    for rows in budgetdata:
        months+= 1
        currentmonth = float(rows[1])
        total += currentmonth
        monthly_diff = currentmonth - previousmonth
        previousmonth = currentmonth
        totalmonthlydiff  += monthly_diff
    
    avgmonthlydiff = totalmonthlydiff/ (months - 1)
    
#pybank answers:
print('financial analysis')
print(f"number of months: {months}")
print(f"Total $ amount: {total}")
print(avgmonthlydiff)
    
