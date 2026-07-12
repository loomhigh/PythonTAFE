
'''
Author: Wyatt Teakle

Project to extract User data from Monica JSON Export.
And express it as a CSV file.
'''

print("Monica JSON to CSV extractor")

#'''
#
import os
import json

current_dir = os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles"

json_file = input("enter Absolute path to json file ")

with open(json_file,"r") as data: json_contents = data.read()

json_to_python = json.loads(json_contents)

           # 
    

print(json_to_python)


#'''