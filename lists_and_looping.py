# Python Lists and Loops
# Created by Nathan Jennings
# Created on:  05.31.2015
# Updated on:  05.31.2015
# Copyright: 2015

# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

'''
Python lists, ArcGIS List routines, and Looping

This script shows examples of creating and using a Python list
and looping over elements in the list using a for and while loop.

ArcGIS list routines are also implemented.

Change the workspace path as needed to run the script

'''



import arcpy, sys, os, datetime



# variables

# a Python List of strings
aPythonList = ['a', 'b', 'c', 'd']

print "This is a Python list of values: " + str(aPythonList)

# a for loop
# print out individual values in a list

# a variable used to identify the specific index value in the Python list
indexnum = 0

# aValue is just a variable that will be assigned to an element
# in the Python list when the for loop line is processed

for aValue in aPythonList:

    print "The " + str(indexnum) + " value in the list is: " + aValue

    # the index value will increase by one so the next item
    # in the Python list will be processed.
    indexnum += 1

indexnum = 0

print "\nThe values below are printed by directly using the specific python list index value"

# the same type of loop, but directly using the "index" value of the python list
for aValue in aPythonList:
    print aPythonList[indexnum]   # produces the same result above but
                                  # references the specific index within the list
    indexnum += 1


# creates an empty Python list
aNewList = []

#add an element to the list

aNewList.append("Betty")  # this is element 0
aNewList.append("Wilma")  # this is element 1
aNewList.append("Fred")   # this is element 2
aNewList.append("Barney") # this is element 3

print "Print the all of the strings in the list..."

print aNewList  # prints all of the values in the list within square brackets []

print "Print each element in the list separately..."

indexvalue = 0
for value in aNewList:
    print aNewList[indexvalue]  # accesses and prints each element in the list
    indexvalue += 1


# Some examples of ArcGIS type list routines (see ArcGIS Help on Lists)

# set a workspace to the folder containing GIS data

# Change the workspace path as needed to run the script

arcpy.env.workspace = "C:\\PythonPrimer\\ArcPy_Bytes\\Data"

print "\nCreate a list of feature classes in a workspace and print them out " \
      "using a for loop."

# get a list of feature classes from the workspace
FeatList = arcpy.ListFeatureClasses()

print "\nGetting a list of fields from each feature class and print them out"

print "\nNumber of feature classes in the list: " + str(len(FeatList))

print "\nThe loop will process " + str(len(FeatList)) + " feature classes"

# this loop will iterate for each element in the feature list
for fc in FeatList:
    print fc  # print the name of the feature class
              # found within the workspace above

    fieldlist = arcpy.ListFields(fc)

    for field in fieldlist:
        print field.name # prints the field name only

    # some clever string formatting to print both the feature class and the field name
    for field in fieldlist:
        print "{0} " "{1}".format(fc, field.name)  # prints the feature class name
                                                   # and the field name separated by a space


# list all of the files in the workspace
# the list will contain all of the individual files in the workspace defined above

print "\nCreate a list of individual files in a workspace and print them out \n" \
      "using a for loop."
filelist = arcpy.ListFiles()

for f in filelist:
    print f

# while loop example

print filelist[indexnum]

indexnum = 0
print "Length of filelist is: " + str(len(filelist))

print "\nPrint only shapefile names (.shp) from a file list using while loop..."

while indexnum < len(filelist): # set up a condition to be true to implement the while loop
                                # notice indexnum is 0 before the loop begins
                                # so that the initial while loop condition is true
    
    if filelist[indexnum][-4:] == ".shp":
        print filelist[indexnum] # print only the shapefiles to the Python Shell

    indexnum += 1


print "\nPrint shapefile names (.shp) by using a wild card in the arcpy.ListFiles \n" \
      "routine and a for loop..."

filelist = arcpy.ListFiles("*.shp") # limit the files to only only those ending in ".shp"

for f in filelist:  
    print f          # prints the same shapefile names as the while loop
