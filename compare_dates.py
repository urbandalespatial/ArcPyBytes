# Compare dates after string conversion

# Created by Nathan Jennings
# Created on:  05.31.2015
# Updated on:  05.31.2015
# Copyright: 2015

# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

'''
Converts two strings to date format, then uses an if statement
to test to determine if one date is earlier than another

Different date formatting can be used for different kinds of date formats
See python.org or other Python resources such as stack exchange for more details.

'''


import time

a = '07/01/2015'
b = '09/04/2014'

datea = time.strptime(a, "%m/%d/%Y")
dateb = time.strptime(b, "%m/%d/%Y")

# compare dates

if datea < dateb:
    print "date a is earlier than date b"

elif dateb < datea:
    print "date b is earlier than date a"

