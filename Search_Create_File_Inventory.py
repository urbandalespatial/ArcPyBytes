# Search and Create a Simple File Inventory
# Creates an inventory of ArcReader (.pmf) files
# and adds them to a file geodatabase table using an insert cursor.

# Created by Nathan Jennings
# Created on: 01.15.15
# Updated on: 01.15.15
# Copyright: 2015

# www.urbandalespatial.com
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

# Sourced code references.  Accessed 01.15.15

# https://geonet.esri.com/thread/23536
# http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
# http://stackoverflow.com/questions/121025/how-do-i-get-the-modified-date-time-of-a-file-in-pythonwww.urbandalespatial.com



import os, arcpy, fnmatch, time

# change this as required
rootfolder = ""


# change this as required
ARTable = "\\ArcReaderAppsInventory.gdb\\ARInventory"


fileList = []
filecount = 0

print "starting..."

irows = arcpy.InsertCursor(ARTable)

for root, dirs, files in os.walk(rootfolder):
    
    for fileName in files:
        
        if fnmatch.fnmatch(fileName, "*.pmf") == True:
            
            print str(os.path.join(root, fileName))
            print root
            print fileName
            print "last modified: %s" % time.strftime("%m/%d/%Y", time.localtime(os.path.getmtime(os.path.join(root, fileName))))
            fDate = time.strftime("%m/%d/%Y", time.localtime(os.path.getmtime(os.path.join(root, fileName))))

            row = irows.newRow()
            row.ARPath = root
            row.ARFileName = fileName
            row.DateModified = fDate

            irows.insertRow(row)

            filecount += 1

print "Number of pmf files: " + str(filecount)

del irows
