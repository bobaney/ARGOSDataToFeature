##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: robert.baney@duke.edu (for ENV859)
##---------------------------------------------------------------------

#Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = '../Data/ARGOSData/1997dg.txt'
outputFC = '../Scratch/ARGOStrack.shp'
outputSR = arcpy.SpatialReference(54002)
arcpy.env.overwriteOutput = True

## Prepare a new feature class to which we'll add tracking points
# Create an empty feature class; requires the path and name as separate parameters
outPath,outName = os.path.split(outputFC)
arcpy.CreateFeatureclass_management(outPath, outName,'POINT','','','',outputSR)

# Add TagID, LC, IQ, and Date fields to the output feature class
arcpy.AddField_management(outputFC,"TagID","LONG")
arcpy.AddField_management(outputFC,"LC","TEXT")
arcpy.AddField_management(outputFC,"Date","DATE")

#Open the ARGOS data file for reading
inputFileObj = open(inputFile, 'r')

#Get the first line so we can loop
lineString = inputFileObj.readline()
while lineString:

    if "Date :" in lineString:

        #Split the line into a list
        lineList = lineString.split()

        #Get attributes from first line
        tagID = lineList[0]

        #Get the next line
        line2String = inputFileObj.readline()
        line2Data = line2String.split()

        #Get attributes from second line
        obsLat = line2Data[2]
        obsLon = line2Data[5]
        date = lineList[3]
        time = lineList[4]
        lc = lineList[7]
        
        #Print results
        print(tagID, obsLat, obsLon, date, time, lc)

        # Construct a point object from the feature class
        obsPoint = arcpy.Point()
        obsPoint.X = obsLon
        obsPoint.Y = obsLat
       
    #Get the next line
    lineString = inputFileObj.readline()

#Close the file object
inputFileObj.close()