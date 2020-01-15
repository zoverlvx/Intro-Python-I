"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# get the args
args = sys.argv

today = datetime.now()
month = today.month
year = today.year

tc = calendar.TextCalendar()

# if there are no args
if len(args) == 1:
    # print calendar for current month
    tc.prmonth(year, month)
# if there's 1 arg
elif len(args) == 2:
    # assume it's the month and print cal for that month
    month = int(args[1])
    tc.prmonth(year, month)
# if there are 2 args, assume it's the month/year
elif len(args) == 3:
    # print cal for that month/year
    month = int(args[1])
    year = int(args[2])
    tc.prmonth(year, month)
else:
    print("Input should be in this format: `14_cal.py month [year]`")
