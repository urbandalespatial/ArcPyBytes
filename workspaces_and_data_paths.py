# Workspaces and Data Paths
# Created by Nathan Jennings
# Created on:  05.31.2015
# Updated on:  05.31.2015
# Copyright: 2015

# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

'''
Simple variable definitions

Change data paths as needed throughout the script

'''


import arcpy, os


# set the current workspace to a folder

# change the path as needed
arcpy.env.workspace = "C:\\PythonPrimer\\ArcPy_Bytes\\Data"


# get a list of all feature classes from the workspace

FeatList = arcpy.ListFeatureClasses()

print "\nNumber of feature classes in the list: " + str(len(FeatList))

print "\nThe loop will process " + str(len(FeatList)) + " feature classes"

# this loop will iterate for each element in the feature list
for fc in FeatList:
    print fc  # print the name of the feature class
              # found within the workspace above

# limit the feature class list to only shapefiles in the workspace

FeatList = arcpy.ListFeatureClasses("*.shp")

print "\nListing only shapefiles..."

for fc in FeatList:
    print fc



# set the current workspace to a file geodatabase

# change the path as needed
arcpy.env.workspace = "C:\\PythonPrimer\\ArcPy_Bytes\\Data\\aGeodatabase.gdb"

# Remember, file geodatabase feature classes do not have an "extension"
# feature classes are not "files" in a file geodatabase, just feature classes
# a file geodatabase feature class is a type of feature class format
# shapefiles is another feature class format

print "\nListing all feature classes in workspace..."

FeatList = arcpy.ListFeatureClasses()

for fc in FeatList:
    print fc

# this list will contain only "polygon" type feature classes in the current worksapce

print "\nListing only polygon feature classes in workspace..."
FeatList = arcpy.ListFeatureClasses("", "Polygon")

for fc in FeatList:
    print fc



# change the path as needed
print "\nChanging a new datapath..."

datapath = r'c:\temp'

print "\nThe new data path is: " + datapath

fc = os.path.join(datapath, 'addresses.shp')

print "\nUsing the new data path"

print fc
