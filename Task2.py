"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def get_problemtwo(call_log):
    '''Takes in caller log from 2016 and outputs the longest conversation duration initiating caller'''
    # Biggest talker aka longest call
    biggest_talker = []

    # Record the longest duration
    longest_duration = 0

    # Columns extracted
    incoming_number, duration = 0, 3

    # Assign Logs
    calls = call_log

    # Check Call log
    for entry in calls:
        longer_call = entry[duration] > longest_duration
        if longer_call:
            biggest_talker = entry[incoming_number]
            longest_duration = entry[duration]

    # Print Solution
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(biggest_talker,longest_duration))

    return 0


get_problemtwo(calls)
