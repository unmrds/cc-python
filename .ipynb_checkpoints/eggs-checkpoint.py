#!/usr/bin/env python

import csv

# create an empty list that will be filled with the rows of data from the CSV as dictionaries
csv_content = []

# open and loop through each line of the csv file to populate our data file
with open('aaj1945_DataS1_Egg_shape_by_species_v2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lineNo = 0
    for row in csv_reader:             # process each row of the csv file
        csv_content.append(row)
        if lineNo < 3:                 # print out a few lines of data for our inspection
            print(row)
        lineNo += 1

# create some empty lists that we will fill with values for each column of data
order = []
family = []
species = []
asymmetry = []
ellipticity = []
avglength = []
        
# for each row of data in our dataset write a set of values into the lists of column values
for item in csv_content:
    order.append(item['\ufeffOrder'])
    family.append(item['Family'])
    species.append(item['Species'])
    
    # deal with issues 
    try:
        asymmetry.append(float(item['Asymmetry']))
    except:
        asymmetry.append(-9999)
        
    try:
        ellipticity.append(float(item['Ellipticity']))
    except:
        ellipticity.append(-9999)
    
    try:
        avglength.append(float(item['AvgLength (cm)']))
    except:
        avglength.append(-9999)

print()
print()

# Calculate and print some statistics
mean_asymmetry = sum(asymmetry)/len(asymmetry)
print("Mean Asymmetry: ", str(mean_asymmetry))
mean_ellipticity = sum(ellipticity)/len(ellipticity)
print("Mean Ellipticity: ", str(mean_ellipticity))
mean_avglength = sum(avglength)/len(avglength)
print("Mean Average Length: ", str(mean_avglength))

# What's wrong with these results? What would you do next to fix the problem?