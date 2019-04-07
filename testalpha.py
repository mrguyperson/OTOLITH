# -*- coding: utf-8 -*-
"""
Created on Sun Apr 07 20:59:02 2019

@author: Ted
"""

import csv

dataDict = {}
sampleOne = []
sampleTwo = []

with open('Ted 05-31-2012.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for index, row in enumerate(reader):
        if row[0] = '1':
            #otherSample.add()
            #sampleData = sampleData
        else: 
            sampleOne.append(row)
            
            
csvFile.close()

print(dataDict['13354'])