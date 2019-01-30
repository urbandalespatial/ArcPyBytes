# Numbers
# Created by Nathan Jennings
# Created on:  05.31.2015
# Updated on:  05.31.2015
# Copyright: 2015

# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

import arcpy, os, sys, datetime


a = 1.0

b = 2.10

c = 3.001


d = a + b + c

print d # prints the sum

numbers = [10.10, 0.12345678, 2, 10, 5.9, 6.6667, 9999999.99998]

# formatting numbers as strings
# :30 - represents the total number of characters in the string
# .4f - represents the number of decimal places on the right side of the decimal

sum = 0

for aNumber in numbers:
    print "{:30.4f}".format(aNumber)

    sum += aNumber
        
print "The sum of the numbers is: " + str(sum)

a = 8
b = 4

print a / b # equals 2
print b / a # equals 0 (because both numbers are integers)

a = 8.0
b = 4

print a / b # equals 4.0 becaus a is a float (i.e. decimal number)
print b / a # equals 0.5 becaues a is a float (i.e. decimal numer)
    

# a range of numbers
arange = range(1, 11) # numbers between 1 and 10

sum = 0.0 # define as a float so the proper math can be computed

for i in arange: # numbers between 1 and 10
    print i
    sum += i

print "The sum is: " + str(sum)

avg = sum/(len((arange)))  # need to get the length,
                           # since arange is a list of values between
                           # 1 and 10
                           
print "The average of the numbers is: " + str(avg)



