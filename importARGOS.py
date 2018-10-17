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
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

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
        print(tagID, obsLat, obsLon, date, time, lc)
        break
    #Get the next line
    lineString = inputFileObj.readline()

#Close the file object
inputFileObj.close()