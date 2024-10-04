# CSV Data Filter to JSON

Takes data from a CSV file and writes the data to a JSON file that meets the conditions

## Table of Contents

* [Overview](#Overview)
* [Installation](#Installation)
* [Usage](#Usage)

## Overview

This software will take in an input of a csv file and 3 conditions which will then copy any data that meets these conditions into a json file.
The input is taken in as a comand line input and saved in a file called output.json.

## Installation

Install the software to your local system using GitHub clone

* Navigate to the Code button
* Copy the URL either SSH or HTTPS
* Open termial and navigate to the directory the clone will go in
* Write git clone and paste the URl

```bash
  $ git clone https://github.com/tylerbeckb/CSV-To-JSON-Pipeline
```

* Deleted the sample csv and json files

## Usage

After installation you will be able to use the software for your own files.

* Needs a command line input of the csv file name and the name of each header in the csv file you want to test for

```bash
$ python3 main_pipeline.py name.csv header
```

* Program will ask for inputs for every header you put in 
* You need to input the data in the csv file you want to filter for the header. It is case sensitive
* Input the information and the data will be saved in a new json file

## Found a bug?

Use the issues tab to submit any issues that you find. It will be appreciated.
