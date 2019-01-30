# Strings
# Created by Nathan Jennings
# Created on:  05.31.2015
# Updated on:  05.31.2015
# Copyright: 2015

# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

'''
Simple sting variable definitions

The folder and geodatabse definitions may or may not occur on disk,
since this code does not check to see if the folder or geodatabase exists

The variables are simply definitions to illustrate the use of strings.

'''

import arcpy, sys, os, datetime



# variable definitions

# simple string definitions

phrase = "My name is: "
myName = "Nate"   # change this to your name

# combine strings together and print them out
print phrase + myName


# a variable defined to the string that represents the name a folder
#datapath = "c:\\pythonprimer\\ArcPyBytes\\Data\\"
datapath = "C:\\PythonPrimer\\ArcPy_Bytes\\Data\\"
outpath = "c:\\pythonprimer\\ArcPy_Bytes\\MyData\\"

# a variable defined to the string that represents the name of a geodatabase
gdbpath = "c:\\pythonprimer\\ArcPy_Bytes\\data\\aGeodatabase.gdb\\"

# a variable defined to the string that represents the name of a shapefile
aShapefileName = "City_Facilities.shp"


# a variable defined to the string that represents the full path of
# the folder and shapefile feature class

city_facilities = os.path.join(datapath, aShapefileName)

print city_facilities

# concatentate two strings together
# the "\n" adds a new line before the string is printed

print "\nThe full path of the shapefile feature class using the Python os.path.join routine is: " + city_facilities

# this is produces the same result as the previous line
city_facilities2 = datapath + aShapefileName

print city_facilities2

print "\nThe full path of the shapefile feature class using a simple string concatentation is: " + city_facilities


# query definitions

# a variable defined as the name of a specific value in a feature class field
facility = "SITE - Community Center"

# LabelClass is a representative field name
# (see the City_Facilities.shp file) in the ArcPyBytes\Data folder
 

# a variable defineds as the "query string" (i.e. where clause) for a prospective query statement
# that might be used in a SelectLayerByAttribute or Cursors routine

query = """"LabelClass" = '""" + facility + """'"""

print query



# Basic String Functions (can be used with ArcGIS Python programming)



# using the variable aShapefile which is assigned to the string "City_Facilities.shp"

# get the number of characters in a string
# notice that the length is converted (i.e. cast) to a string before concatenating with
# the rest of the characters in the sentence

print "The number of characters in " + aShapefileName + " is: " + str(len(aShapefileName))

# individually print out the individual characters in the string

index = 0
for char in aShapefileName:
    print "The character index is: " + str(index) + " and the character is " + aShapefileName[index]
    index += 1

# Get the first 4 characters

print aShapefileName[0:4] # produces "City"
print aShapefileName[:4] # produces "City"

# Get the middle characters beginning with the 5th indexed (actually the 6th character) in the string
# and ending at the 15th index (i.e. 16th character in the string

print aShapefileName[5:15] # produces "Facility"

# Get the last 3 characters in the string

print aShapefileName[16:] # produces "shp"

# Get the last 4 characters in the string

print aShapefileName[15:] # produces ".shp"

print aShapefileName[-4:] # also produces ".shp" (get the last for characters from the right)








