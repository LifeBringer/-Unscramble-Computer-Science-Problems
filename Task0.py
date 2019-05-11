"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def get_problemzero(calls, texts):
    # Records to locate
    first_text, last_call = 0, -1
 
    # Print Solution
    print("First record of texts, {0} texts {1} at time {2}".format(*texts[first_text]))
    print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(*calls[last_call]))
    return 0

get_problemzero(calls, texts)
