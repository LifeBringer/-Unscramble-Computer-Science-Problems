# Unscramble-Computer-Science-Problems
Project for better understanding of Data Structures &amp; Algorithms

## Project Overview
In this project, I completed five tasks based on a fabricated set of calls and texts exchanged during September 2016. I used Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, I performed run time analysis of your solution and determine its efficiency.

## About the data
The text and call data are provided in csv files. In each file, the data is read and stored as lists of lists.

Each sub-list of the list of texts is structured in this way:

a text = [Sending telephone number (string),
        receiving telephone number (string),
        timestamp of text message (string)]
        
Each element in the list of phone calls is structured in this way:

a call = [   Calling telephone number (string), 
        receiving telephone number (string), 
        start timestamp of telephone call (string),
        duration of telephone call in seconds (string)]
        
All telephone numbers are 10 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

- Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0.
- Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9.
- Telemarketers' numbers have no parentheses or space, but start with the code 140.
