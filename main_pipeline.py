import json
import csv

def retrieve ( header ,data, type, score_range, region ):
    pass

def save_json():
    pass

# Creates list variable
header = []
data = []
# Opens csv file
with open( 'wine_data.csv') as file:
    # Reads the headers
    header = next ( file )
    # Adds all the data to a list
    for row in file:
        data.append ( row )

