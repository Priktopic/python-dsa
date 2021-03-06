"""
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Import statement
import csv 

# Open 'texts.csv' file
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Print the first record of texts along with time
print("First record of texts, {0} texts {1} at time {2}".format(texts[0][0],texts[0][1],texts[0][2]))

"""
'texts[0]' prints first row of the csv file. 'texts[0][0]' prints first element of the first row, 'texts[0][1]' prints second element of first row 
and 'texts[0][2]' prints 3rd element of first row. Similar procedure is followed for calls too.
"""

# Open 'calls.csv' file
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Print the last record of calls along with time
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(calls[-1][0],calls[-1][1],calls[-1][2],calls[-1][3]))
