
'''
Program:        Wyatts Simple Contact Manager!
Description:    The application must allow the user to enter contact details (names, phone number and email) and save the task to a text file. 
It will create the text file if it doesn’t already exist.  The user will be able to view a list of contacts and then choose to view their details.
The application will save the contact’s full name and phone number. the phone number should be a string of exactly 10 characters. 
The contact will either be flagged as Family or Friend.  There will also be an option to delete any particular contact. 
If you want to stand out from the other applicants for the junior programming position you can add the following advanced feature, 
but this are optional:  
• Users have the option display just Friends or just Family

Author:         Wyatt Teakle
Date:           June 2026
Version:        1.0

Copyright (c) 2025 CITE Managed Services - All Rights Reserved 
(For github users, the above is there for TAFE purposes only, this is an Open Source project)
'''

## Setting up working directory, making sure it is always placed relative to the script file.
import os
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles"):
    os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles")
current_dir = os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles"
print("Files are stored at: " + current_dir + "")

print("Welcome to Project A, the Simple Contacts Application!")

# Creating the Contacts file, which will be formatted like a CSV
contacts_list = [
    os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles/Contacts.txt"

]
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles/Contacts.txt"):
    contacts_list = f"contact_id\t contact_type\t first_name\t last_name\t ph_num\t email\n"
    with open(current_dir + "/Contacts.txt","w+") as text_data:
        text_data.write(str(contacts_list))


# gathering data via user input
contact_id = 0 #this needs to be updated to reflect saved file ID
add_new_contact = "y"
while add_new_contact == "y":
    contact_id = contact_id + 1
    contact_type = input("[1] Friend \n[2] Family? ")
    first_name = input("What is this persons first name? ")
    last_name = input("What is this persons last name? ")
    ph_num = input("What is their number? ")
    email = input("what is their email? ")

    contacts_list = f"{contact_id}\t {contact_type}\t {first_name}\t {last_name}\t {ph_num}\t {email}\n"

    ## Inputting data so that it respects csv format
    with open(current_dir + "/Contacts.txt","a") as text_data:
        for record in contacts_list:
            text_data.write(contacts_list)
        print("\nData Saved Successfully")

    ## Changes value of add_new_contact so it will always be the lowercase first letter of the input
    ## Input can be any variation of "Yes/Y/y/YES/yes" and it will return "y"
    add_new_contact = input ("Would you like to add another? (Y/N) ")
    add_new_contact = str.lower(add_new_contact[0])

with open(current_dir + "/Contacts.txt","r") as text_data:
     for record in text_data:
        print(record[1] + record[2])