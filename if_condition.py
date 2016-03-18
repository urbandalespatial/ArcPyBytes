# Python Conditional Statements
# Created by Nathan Jennings
# Created on:  01.18.2016
# Updated on:  01.18.2016
# Copyright: 2016

# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007


import arcpy, sys, os, datetime



# variables

aName = "ArcGIS" # or 'ArcGIS'

aNumber = 3  # change the number to perform different tests 

# aPythonList = ['a', 'b', 'c', 'd']

# datapath = "c:\\temp\\pythoncode\\"


#x = aName 

# remove this comment, comment out the line above, save the program, and re-run script
# to see how the code below changes

x = "just GIS"  # change x to test the if statement below

if x == "ArcGIS":

    print "The name is: " + aName


else:

    print x + " is a different name"


if aNumber > 0:

    print "The number is a positive number"

    if math.fmod(aNumber,2) == 0:   # fmod (i.e. modulo) - a way to determine if there
                                    # is a remainder.  fmod is better than using the %
                                    # e.g. aNumber % 2 and is ok to use with integers
                            
        print "The number is even"

    elif math.fmod(aNumber,2) <> 0:
        print "The number is odd"

else:
    print "The number is negative"
