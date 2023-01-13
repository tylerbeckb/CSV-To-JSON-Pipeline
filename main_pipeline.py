import json
from csv import DictReader
import sys

def retrieve (data_dict, header_list, condition_list) -> list:
    json_list = []
    # Iterates through all the data
    for items in data_dict:
        count = 0
        # Iterates through all the conditions
        for header in header_list:
            # Checks if it meets the condition
            if items[header] == condition_list[count]:
                found = True
            else:
                found = False
            count = count + 1
        # If it meets every condition it gets added to a list
        if found:
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
        print('Enter the condition for the column:', condition)
        str_input = input()
        condition_data.append(str_input)

    # Calls function to retrieve the data that meets the conditions
    json_data = retrieve(list_of_data, conditions, condition_data)
    # Calls the function that writes data to a json file
    save_json(json_data)
