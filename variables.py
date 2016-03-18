# Variables
# Created by Nathan Jennings
# Created on:  05.31.2015
# Updated on:  05.31.2015
# Copyright: 2015

# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

'''
Simple variable definitions

'''

import arcpy, sys, os, datetime



# variables

aName = "ArcGIS" # or 'ArcGIS'

aNumber = 1

aPythonList = ['a', 'b', 'c', 'd']

datapath = "c:\\temp\\pythoncode\\"


print "This is a name: " + aName

print "This is a number: " + str(aNumber)

print "This is a Python list of values: " + str(aPythonList)

print "This string represents a data path to a folder: " + datapath



# a for loop
# print out individual values in a list

indexnum = 0
for aValue in aPythonList:

    print "The " + str(indexnum) + " value in the list is: " + aValue

    indexnum += 1
