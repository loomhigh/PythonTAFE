
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
#contacts_path = os.path.dirname(os.path.realpath(__file__)) + "/output/data.txt"
contacts_path = "/home/personal/Downloads/data.txt"


json_file = input("enter Absolute path to json file ")

#TEMPORARY code for easy testing
if json_file == "":
    json_file = ("/home/personal/Downloads/monica.json")

with open(json_file,"r") as data: json_contents = data.read()

json_to_python = json.loads(json_contents) #dict
json_account = json_to_python["account"] #dict
json_data = json_account["data"] #list
json_contacts = json_data[1]

print(type(json_contacts))

def json_extract_contacts(tag_filter):
  if type(values["properties"].get("tags")) is list:
      while  tag_filter in values["properties"].get("tags") or tag_filter == "":
        contacts_address = ""
    
# Get contacts Name and Address, leaving invalid data blank
        contacts_first_name = str(values["properties"].get("first_name"))
        if contacts_first_name == "None":
            contacts_first_name = ""
        contacts_last_name = str(values["properties"].get("last_name"))
        if contacts_last_name == "None":
            contacts_last_name = ""
        contacts_name = str(contacts_first_name)+" "+str(contacts_last_name)
        if contacts_last_name == "":
           contacts_name = str(contacts_first_name)+""+str(contacts_last_name)
        if contacts_name == "None":
           contacts_name = ""
        contacts_tags = ("\'"+", ".join(values["properties"].get("tags"))+"\'")
        if contacts_tags == "None":
            contacts_tags = ""
        contacts_notes = "\'"+str(values["properties"].get("description"))+"\'"
        for data_type in values["data"]:
            if data_type["type"] == "address":
                contacts_street = data_type["values"][0]["properties"].get("street")
                contacts_city = data_type["values"][0]["properties"].get("city")
                contacts_postal = str(data_type["values"][0]["properties"].get("province"))+" "+str(data_type["values"][0]["properties"].get("postal_code"))
                contacts_address = "\'"+str(contacts_street)+", "+str(contacts_city)+", "+str(contacts_postal)+"\'"


    #create CSV line and return as output
        contacts_output = str(contacts_name)+","+str(contacts_address)+","+str(contacts_notes)+", "+str(contacts_tags)
        return(contacts_output)
#Function to release Contacts
tag_filter = input("What tag do you want to filter for? ")
for values in json_contacts["values"]:
    if json_extract_contacts(tag_filter) != None:
        towrite = json_extract_contacts(tag_filter)
        with open(contacts_path,"a") as contacts:
            print(towrite)
            contacts.write("%s\n" % towrite)
    time.sleep(0.01)
#print(json_contacts)
#print(json_to_python["type"])
