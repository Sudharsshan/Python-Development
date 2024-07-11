'''
DATE: 10-07-2024
TASK: Write a python program to manage database using JSON
'''
import json
import numpy as np

# Ask user for the necessary data:
# Name, Registered No., branch and GPA
studentNo = int(input('Please enter number of students: '))

# Declare the user data dictionary
userDictionary = [['' for x in range(4)] for y in range(studentNo)]
askData = ['name', 'registered no.','department','CGPA']

# Collect the user data
for totalStudentNo in range(studentNo):
    for indent in range(4):
        askUser = 'Please enter student '+str(totalStudentNo)+'\'s '+str(askData[indent])+' '
        userInput = input(askUser)
        userDictionary[totalStudentNo][indent] = userInput

# Assign user data along with respective IDs
for currentStudentNo in range(studentNo):
    for indent in range(4):
        userDictionary[currentStudentNo][indent] = 0
print(userDictionary)