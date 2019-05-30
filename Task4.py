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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order
with no duplicates.
"""


def get_problemfour(call_log, text_log):
    '''Takes call log and text log and provides a list of possible
    telemarketers'''
    # List of area codes in Bangalore
    suspect_list = set()
    texter_textee_list = get_list_of_texters_textees(text_log)
    answering_list = get_list_of_answering_nums(call_log)

    # Columns extracted
    incoming_number = 0

    # Assign Logs
    calls = call_log

    # Check Call log
    for entry in calls:
        number_on_trial = entry[incoming_number]
        if number_on_trial not in texter_textee_list and number_on_trial not in \
                answering_list:
            suspect_list.add(number_on_trial)

    # Output
    print("These numbers could be telemarketers: ")
    suspect_list = sorted(suspect_list)
    for suspect in suspect_list:
        print(suspect)

    return -1


def get_list_of_texters_textees(text_log):
    # Catalog of unique numbers
    catalog = set()

    # Columns extracted
    incoming_number, answering_number = 0, 1

    # Assign Logs
    texts = text_log

    # Check Text log
    for entry in texts:
        catalog.add(entry[incoming_number])
        catalog.add(entry[answering_number])

    return catalog


def get_list_of_answering_nums(call_log):
    # Catalog of unique numbers
    answer_catalog = set()

    # Columns extracted
    answering_number = 1

    # Assign Logs
    calls = call_log

    # Check Text log
    for entry in calls:
        answer_catalog.add(entry[answering_number])

    return answer_catalog

get_problemfour(calls, texts)
