# -*- coding: utf-8 -*-
"""
Created on Sun Apr 07 19:59:49 2019

@author: Ted
"""

import csv

dataDict = {}

with open('Ted 05-31-2012.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for index, row in enumerate(reader):
        dataDict[str(index)] = row

csvFile.close()

print(dataDict['13354'])