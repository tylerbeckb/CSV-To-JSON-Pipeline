import json
from csv import DictReader

def retrieve (data_dict, variety, min_score, max_score, region ) -> list:
    json_list = []
    # Iterates through all the data
    for items in data_dict:
        # Checks if the type matches
        if items['variety'] == variety:
            # Checks if the region matches
            if items['region'] == region:
                # Checks if the rating is in the range
                if int(float(items['rating'])) >= min_score & int(float(items['rating'])) <= max_score:
                    # Adds the data to the list
                    json_list.append(items)
    return json_list

def save_json(json_list) -> None:
    # Opens the json file to write too
    output = open('output.json', 'w')
    # Converts the list into a string
    json_string = json.dumps(json_list)
    # Writes it to the file
    output.write(json_string)
    # Closes the file
    output.close()

# Creates list variable
json_data = []
# Opens csv file
with open('wine_data.csv', 'r') as file:
    # Adds all the data to a dictionary
    dict_reader = DictReader(file)
    list_of_data = list(dict_reader)

# Asks for user inputs for each condition
wine_variety = input( 'Enter the wine type to find: ' )
min_rating = int(input( 'Enter an integer for the minimum wine score to find: ' ))
max_rating = int(input( 'Enter an integer for the maximum wine score to find: ' ))
wine_region = input( 'Enter the region of wine to find: ' )

# Calls function to retrieve the data that meets the conditions
json_data = retrieve(list_of_data, wine_variety, min_rating, max_rating, wine_region)
# Calls the function that writes data to a json file
save_json(json_data)
