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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_problemone(call_log, text_log):
    '''Takes in logs and outputs number of unique numbers.'''
    # Catalog of unique numbers
    catalog = []

    # Columns extracted
    incoming_number, answering_number = 0, 1

    # Assign Logs
    calls = call_log
    texts = text_log

    # Check Call log
    for entry in calls:
        if entry[incoming_number] not in catalog:
            catalog.append(entry[incoming_number])
        if entry[answering_number] not in catalog:
            catalog.append(entry[answering_number])

    # Check Text log
    for entry in texts:
        if entry[incoming_number] not in catalog:
            catalog.append(entry[incoming_number])
        if entry[answering_number] not in catalog:
            catalog.append(entry[answering_number])

    # Number of unique entries
    count = len(catalog)

    # Print Solution
    print("There are {} different telephone numbers in the records.".format(count))
    
    return 0


get_problemone(calls, texts)
