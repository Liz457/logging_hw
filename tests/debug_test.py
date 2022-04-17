import os

""" This checks if the debug log file is created"""
# get the path to the file
path = r'../logs/lizApp.log'

# Check
if os.path.isfile(path):
    print('File exists')

else:
    print('File does not exist')