import json
import csv

def retrieve ( header ,data, type, min_score, max_score, region ):
    pass

def save_json():
    pass

# Creates list variable
header = []
data = []
json_data = []
# Opens csv file
with open('wine_data.csv') as file:
    # Reads the headers
    header = next ( file )
    # Adds all the data to a list
    for row in file:
        data.append ( row )

wine_type = input( 'Enter the wine type to find' )
min_score = int(input( 'Enter an integer for the minimum wine score to find' ))
max_score = int(input( 'Enter an integer for the maximum wine score to find' ))
region = input( 'Enter the region of wine to find' )

json_data = retrieve(header, data, wine_type, min_score, max_score, region)
