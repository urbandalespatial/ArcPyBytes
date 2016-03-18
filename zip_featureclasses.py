# zip shapefile feature classes in workspace
# Created by: Nathan Jennings
#             www.urbandalespatial.com
# Created on: 07.13.2015
# Updated on: 07.13.2015
# Copyright: 2015
# GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

import arcpy, zipfile, os, datetime, time

arcpy.env.workspace = "c:\\temp\\"
zipdir = "c:\\temp"

CURDATE = datetime.date.today().strftime('%m%d%Y')

# can modify if other data types are desired
# or use ListFiles routine or os.walk Python routine
# see AcGIS resources or python.org for more details

shplist = arcpy.ListFeatureClasses()

print "starting zip..."

azipfile = os.path.join(zipdir, "zip" + CURDATE + ".zip")

if arcpy.Exists(azipfile):
    arcpy.Delete_management(azipfile)

# use Python zipfile functionality
# ZIP_DEFLATED adds compression
with zipfile.ZipFile(azipfile, 'a', zipfile.ZIP_DEFLATED) as outzip:

    for shp in shplist:
        rootname = os.path.splitext(shp)

        # splitext returns a Python list of root name and extension
        # rootname[0] is the first element in the list
        # arcpy.ListFiles creates a list based on the rootname
        # of the shapefiles in the folder
        
        filelist = arcpy.ListFiles(str(rootname[0]) + "*")

        for f in filelist:

            # ignore any zipfiles that may be in the folder
            if not f.endswith(".zip"):
                print "printing " + str(f)
            
                outzip.write(f)

outzip.close()

print "finished zipping"
