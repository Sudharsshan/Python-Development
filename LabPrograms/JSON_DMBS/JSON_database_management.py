'''
DATE: 10-07-2024
TASK: Write a python program to manage database using JSON
'''
import json
import numpy as np

# Ask user for the necessary data:
# Name, Registered No., branch and GPA

# Collect the user data
print('Please enter the following details:')
name = input('Name: ')
regNo = int(input('Registered No.: '))
dept = input('Department: ')
CGPA = float(input('CGPA: '))

# Assign user data along with respective IDs in an JSON dictionary
studentDictionary = {
    'name' : name,
    'registeredNo' : regNo,
    'department' : dept,
    'CGPA' : CGPA
}

# Serializing JSON
json_obj = json.dumps(studentDictionary, indent=4)

# Write the data to studentDetails.json file
with open('studentDictionary.json', 'w') as outfile:
    outfile.write(json_obj)

print('Written data into file \'studentDictionary.json')