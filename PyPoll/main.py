#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:


#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# In[14]:


#import csv
import os
import csv

#path to collect data from CSV file
path = 'election_data.csv'

#initialize variables
total_votes = 0
khan_tally = 0
correy_tally = 0
li_tally = 0
otooley_tally = 0
winner = ""

#open CSV file and make sure it skips first row
with open(path,'r', newline="") as pollcsv:
    election_data = csv.reader(pollcsv, delimiter=",")
    header = next(election_data)
    first_row = next(election_data)
    #sets starting point for all vote tallies
    total_votes += 1
    khan_tally += 1
    correy_tally += 1
    li_tally += 1
    otooley_tally += 1
    #for each line in the csv tally the vote to the total vote, note who the vote was cast for and add that vote to the appropriate tally
    for row in election_data:
        total_votes +=1
        if row[2] == "Khan":
            khan_tally += 1
        elif row[2] == "Correy":
            correy_tally += 1
        elif row[2] == "Li":
            li_tally += 1
        elif row[2] == "O'Tooley":
            otooley_tally +=1


# In[15]:


#calculate percentage of vote and assign to variables
khan_percent = round(((khan_tally/total_votes)*100),3)
correy_percent = round(((correy_tally/total_votes)*100),3)
li_percent = round(((li_tally/total_votes)*100),3)
otooley_percent = round(((otooley_tally/total_votes)*100),3)


# In[16]:


#create dictionary of winners and their number of votes, then use max to find the key with the largest value
total_list = {'Khan': khan_tally,'Correy': correy_tally,'Li': li_tally,'OTooley': otooley_tally}
winner = max(total_list, key=lambda key: total_list[key])


# In[17]:


#print results and export to txt
with open("results.txt", "a") as write_file:
    print(f'Election Results', file=write_file)
    print(f'-------------------------', file=write_file)
    print(f'Total Votes: {total_votes}', file=write_file)
    print(f'-------------------------', file=write_file)
    print(f'Khan: {khan_percent}% ({khan_tally})', file=write_file)
    print(f'Correy: {correy_percent}% ({correy_tally})', file=write_file)
    print(f'Li: {li_percent}% ({li_tally})', file=write_file)
    print(f'O\'Tooley: {otooley_percent}% ({otooley_tally})', file=write_file)
    print(f'-------------------------', file=write_file)
    print(f'Winner: {winner}', file=write_file)
    print(f'-------------------------', file=write_file)

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent}% ({khan_tally})')
print(f'Correy: {correy_percent}% ({correy_tally})')
print(f'Li: {li_percent}% ({li_tally})')
print(f'O\'Tooley: {otooley_percent}% ({otooley_tally})')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')


# In[ ]:





# In[ ]:




