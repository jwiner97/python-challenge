#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import csv
import os
import csv

#path to collect data from CSV file
path = 'budget_data.csv'

#initialize variables
total = 0
counter = 0
current = 0
previous = 0
previous_dec = 0
changes = []
current_increase = 0
current_decrease = 0
highest_month = ''
lowest_month = ''

#open CSV file and make sure it skips first row
with open(path,'r', newline="") as bankcsv:
    BankData = csv.reader(bankcsv, delimiter=",")
    header = next(BankData)
    first_row = next(BankData)
    #Setting up total counter which will loop through list and give total P&L as well as count up months
    total = int(first_row[1]) + total
    counter += 1
    #Because our P&L increase and decrease is a comparison, we need to store the previous entry as a variable
    #in this case, the first row of the data
    previous = int(first_row[1])
    previous_dec = int(first_row[1])
    #for loop will loop through all entries in BankData and tick up the counter and total variables. 
    for entry in BankData:
        total = int(entry[1]) + total
        counter += 1
        #Creates a separate changes list to house computed deltas
        changes.append(int(entry[1]) - previous)
        #compare P&L of entry to previous entry and evaluate whether it is larger or smaller than what's stored
        #this will store the largest increase and decrease
        if (int(entry[1]) - previous > current_increase):
            current_increase = (int(entry[1]) - previous)
            highest_month = entry[0]
            previous = (int(entry[1]))
        else:
            previous = int(entry[1])
        if (int(entry[1]) - previous_dec < current_decrease):
            current_decrease = (int(entry[1]) - previous_dec)
            lowest_month = entry[0]
            previous_dec = (int(entry[1]))
        else:
            previous_dec = int(entry[1])


# In[3]:


#Loops through the Changes list created on line 37 above to find total change on beg date and end date
total_change = 0
for row in changes:
        total_change = row + total_change


# In[4]:


#computes average of changes in profit/losses over period
average = round(((total_change)/(counter - 1)),2)


# In[5]:


#print results
with open("results.txt", "a") as write_file:
    print(f'Financial Analysis', file=write_file)
    print(f'----------------------------', file=write_file)
    print(f'Total Months: {counter}', file=write_file)
    print(f'Total: ${total}', file=write_file)
    print(f'Average Change: ${average}', file=write_file)
    print(f'Greatest Increase in Profits: {highest_month} (${current_increase})', file=write_file)
    print(f'Greatest Decrease in Profits: {lowest_month} (${current_decrease})', file=write_file)

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {counter}')
print(f'Total: ${total}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {highest_month} (${current_increase})')
print(f'Greatest Decrease in Profits: {lowest_month} (${current_decrease})')


# In[ ]:




