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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import re

#Problem A start
def get_problemthreeA(call_log):
    '''Takes call log and provides a list of unique numbers in lexilogical order'''
    
    # List of area codes called by Bangalorians
    list_of_codes = []

    # Columns extracted
    incoming_number, answering_number = 0, 1

    # Assign Logs
    calls = call_log

    # Check Call log
    for entry in calls:
      answering_areacode = get_areacode(entry[answering_number])
      bangalore_caller = re.match(r"\(080\)", entry[incoming_number])
      if answering_areacode not in list_of_codes and bangalore_caller:
          list_of_codes.append(answering_areacode)
    
    # Part A Output
    print("The numbers called by people in Bangalore have codes:")
    list_of_codes.sort()
    for area_code in list_of_codes:
      print(area_code)

    return -1


def get_areacode(number):
  '''Extracts Area Code from number provided'''
  pattern = get_areacode_pattern(number)
  assert pattern, "Not a number recognized!"
  area_code = re.search(pattern, number).group(1)
  return area_code


def get_areacode_pattern(number):
  '''Checks numbers against known patterns and returns relevant pattern'''
  fixedline_pattern = r"(\(0[0-9]*\))"
  mobile_pattern = r"([7,8,9][0-9]+)( )"
  telemarketer_pattern = r"(140)"

  pattern_set = (fixedline_pattern, mobile_pattern, telemarketer_pattern)

  for pattern in pattern_set:
    if re.match(pattern, number):
      return pattern

  return None

### Problem B Start
def get_problemthreeB(call_log):
    '''Takes call log and outputs percentage of Bangalore fixed lines calling Bangalore 
    fixed lines versus all Bangalore fixed lines calls'''
    # Record the longest duration
    fixed_to_fixed = 0
    any_fixed = 0

    # Columns extracted
    incoming_number, answering_number = 0, 1

    # Assign Logs
    calls = call_log

    # Check Call log
    for entry in calls:
      incoming_from_banglore = re.match(r"\(080\)", entry[incoming_number])
      answering_from_banglore = re.match(r"\(080\)", entry[answering_number])
      
      # Count scenarios of Banagalore calling others
      if incoming_from_banglore and answering_from_banglore:
        fixed_to_fixed += 1
      elif incoming_from_banglore or answering_from_banglore:
        any_fixed += 1
  

    # Part B Output
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(100.0*fixed_to_fixed/any_fixed))

    return -1

# Process Problem 3
get_problemthreeA(calls)
get_problemthreeB(calls)
