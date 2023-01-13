import json
from csv import DictReader
import sys

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

if __name__ == '__main__':
    # Creates list variable
    json_data = []
    conditions = []
    condition_data = []

    # Opens csv file
    with open(sys.argv[1], 'r') as file:
        # Adds all the data to a dictionary
        dict_reader = DictReader(file)
        list_of_data = list(dict_reader)

    # Loops through all the command line inputs
    for count in range(len(sys.argv)-2):
        # Adds the conditions to a list
        conditions.append(sys.argv[count+2])

    # Asks the user for inputs for each condition
    for condition in conditions:
        condition_data.append(input('Enter the condition for the column', conditions[condition]))

    # Asks for user inputs for each condition
    wine_variety = input( 'Enter the wine type to find: ' )
    min_rating = int(input( 'Enter an integer for the minimum wine score to find: ' ))
    max_rating = int(input( 'Enter an integer for the maximum wine score to find: ' ))
    wine_region = input( 'Enter the region of wine to find: ' )

    # Calls function to retrieve the data that meets the conditions
    json_data = retrieve(list_of_data, wine_variety, min_rating, max_rating, wine_region)
    # Calls the function that writes data to a json file
    save_json(json_data)
