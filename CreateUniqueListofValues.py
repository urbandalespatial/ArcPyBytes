# Create and use list or arrays of unique values

# Created by:  Nathan Jennings
# Created on:  03.26.2017
# Updated on:  03.26.2017
# Copyright: UrbandaleSpatial, 2017
# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

'''
Uses the sacramento_streets.shp file from the Python Primer Chapter05 Data folder.
The source file and data field can be changed as necessary.

2 options to create a unique list of values (i.e. the "CLASS" field)
and then use the list for further geoprocessing
(in this case a SelectLayerByAttribute routine)

A SelectFeatures function performs the primary geoprocessing of the data

1. Create a unique Python List
2. Create a numpy array (arrays are much faster than lists)

'''

import arcpy, numpy

# function to select features and print count to Python Shell
def SelectFeatures(uniqueList):

    for val in uniqueList:

        if arcpy.Exists(streets):
            arcpy.Delete_management(streets)

        arcpy.MakeFeatureLayer_management(fc, streets)
        
        query = """ "CLASS" = '""" + val + """'"""

        arcpy.SelectLayerByAttribute_management(streets, "NEW_SELECTION", query)

        result = arcpy.GetCount_management(streets)
        print str(result) + ' records for street class type ' + val
    


# change path to feature class as required
fc = "c:\\temp\\chapter05\\data\\sacramento_streets.shp"

# variable for feature layer name
streets = 'streets'

t0 = time.clock()


street_types = [] # empty python list to store specific values

with arcpy.da.SearchCursor(fc, 'CLASS') as srows:

    for srow in srows:
        street_types.append(srow[0])  # append a new value to the list
        

uniqueSet = set(street_types)  # create a "set" of unique values.  See "sets" in Python documentation
uniqueList = list(uniqueSet)  # create a list of these values, so we can iterate through the list
                              # for the SelectFeatures function

uniqueList.sort() # sort the list from A-Z (in this case)

print uniqueList

# call the SelectFeatures function
SelectFeatures(uniqueList)

print time.clock() - t0, 'seconds to process a Python list\n'



# same process using a numpy array (could be faster for large datasets)
# numpy options can be found in the Data Access (da) arcpy module

# notice time is just over 1 second compared to a several seconds
# for the cursor process...and you get automatic sorting with the
# numpy array!

t0 = time.clock()

# converts the values in the "CLASS" field to a numpy array
fieldvals = arcpy.da.TableToNumPyArray(fc, 'CLASS')  

# creates a unique list of values from the "CLASS" field
data = numpy.unique(fieldvals['CLASS'])

print data

SelectFeatures(data)

print time.clock() - t0, 'seconds to process numpy array'
