
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
import time #adding sleep command. Purely aesthetic

# output file directory
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/output"):
    os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "/output")
current_dir = os.path.dirname(os.path.realpath(__file__)) + "/output"
contacts_path = os.path.dirname(os.path.realpath(__file__)) + "/output/data.txt"

# Source - https://stackoverflow.com/a/48005385
# Posted by grafi71
# Retrieved 2026-07-12, License - CC BY-SA 3.0


json_file = input("enter Absolute path to json file ")

#TEMPORARY code for easy testing
if json_file == "":
    json_file = ("/home/personal/Downloads/monica.json")

with open(json_file,"r") as data: json_contents = data.read()

json_to_python = json.loads(json_contents) #dict
json_account = json_to_python["account"] #dict
json_data = json_account["data"] #list
json_contacts = json_data[1]
#json
#json_users = json_data[0]

#contact = [json_data,first_name,last_name,ph_num,email,category]   # sets contact to the contact details


#json_output = json_to_python[input("enter desired data ")]
x=0
#with open(contacts_path,"w") as data: data.write(str(json_contacts,sep="\n"))
print(type(json_contacts))
#output_filter = input("what tags do you want to filter for")

contacts_address = ""
for values in json_contacts["values"]:
    for data_type in values["data"]:
        if data_type["type"] == "address":
            contacts_street = data_type["values"][0]["properties"].get("street")
            contacts_city = data_type["values"][0]["properties"].get("city")
            contacts_address = "\'"+str(contacts_street)+" , "+str(contacts_city)+"\'"
    #if condata_type == "address":
    #    contacts_data = values["data"]
    #else:
    #    contacts_address = ""
    #print(contacts_address)
    contacts_name = str(values["properties"].get("first_name")),str(values["properties"].get("last_name"))
    contacts_tags = values["properties"].get("tags")
    contacts_output = str(contacts_name)+","+str(contacts_address)+","+str(contacts_tags)

    print(contacts_output)
    contacts_address = ""
#    for properties in values["properties"]:
#        print(properties.get("first_name"))
    time.sleep(0.2)
#print(json_contacts)
#print(json_to_python["type"])
