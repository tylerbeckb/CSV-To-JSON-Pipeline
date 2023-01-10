import json
import csv

def retrieve (data_list, variety, min_score, max_score, region ) -> list:
    json_list = []
    # Iterates through all the data
    for items in data_list:
        # Checks if the type matches
        if items[3] == variety:
            # Checks if the region matches
            if items[2] == region:
                # Checks if the rating is in the range
                if items[4] >= min_score & items[4] <= max_score:
                    # Adds the data to the list
                    json_list.append(items)
    return json_list

def save_json(json_list):
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

# Asks for user inputs for each condition
wine_variety = input( 'Enter the wine type to find' )
min_rating = int(input( 'Enter an integer for the minimum wine score to find: ' ))
max_rating = int(input( 'Enter an integer for the maximum wine score to find: ' ))
wine_region = input( 'Enter the region of wine to find: ' )

# Calls function to retrieve the data that meets the conditions
json_data = retrieve(data, wine_variety, min_rating, max_rating, wine_region)
save_json(json_data)