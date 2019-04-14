# -*- coding: utf-8 -*-
"""
Created on Sun Apr 07 20:59:02 2019

@author: Ted
"""

import csv

sampleNames = ["MACS3-2", "Pellet-2"]
currentSample = []
dataDict = {}

with open('Ted 05-31-2012.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in enumerate(reader):
        if row[1][0] in sampleNames:
            dataDict[currentSample[0][0]] = currentSample
            currentSample = []
        currentSample.append(row[1])

csvFile.close()

for key in dataDict:
    print("\n" + key + ": \n")
    for row in dataDict[key]:
        print("" + key + ": " + " ".join(row))
