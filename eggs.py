#!/usr/bin/env python

import csv

# create an empty list that will be filled with the rows of data from the CSV as dictionaries
csv_content = []

# open and loop through each line of the csv file to populate our data file
with open('aaj1945_DataS1_Egg_shape_by_species_v2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:             # process each row of the csv file
        csv_content.append(row)

print("keys: " + ", ".join(csv_content[0].keys()))

print()
print()

# define a function that can extract a named column from a named list of dictionaries
def extract_column(source_list, source_column):
    new_list = []
    for item in source_list:
        try:
            new_list.append(item[source_column])
        except:
            new_list.append(None)
    print(source_column + ": " + ", ".join(new_list[0:3]))
    return(new_list)
            
order = extract_column(csv_content, 'Order')
family = extract_column(csv_content, 'Family')
species = extract_column(csv_content, 'Species')
asymmetry = extract_column(csv_content, 'Asymmetry')
ellipticity = extract_column(csv_content, 'Ellipticity')
avgLength = extract_column(csv_content, 'AvgLength (cm)')
noImages = extract_column(csv_content, 'Number of images')
noEggs = extract_column(csv_content, 'Number of eggs')

print()
print(order[0:3])
print(family[0:3])
print(species[0:3])
print(asymmetry[0:3])
print(ellipticity[0:3])
print(avgLength[0:3])
print(noImages[0:3])
print(noEggs[0:3])

# Calculate and print some statistics
print()
mean_asymmetry = sum(map(float, asymmetry))/len(asymmetry)
print("Mean Asymmetry: ", str(mean_asymmetry))
mean_ellipticity = sum(map(float, ellipticity))/len(ellipticity)
print("Mean Ellipticity: ", str(mean_ellipticity))
mean_avglength = sum(map(float, avgLength))/len(avgLength)
print("Mean Average Length: ", str(mean_avglength))