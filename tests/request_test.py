import os

""" This checks if the request log file is created"""
# get the path to the file
path = r'../logs/request.log'

# Check
if os.path.isfile(path):
    print('File exists')

else:
    print('File does not exist')