
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

'''
#TASK DETAILS:

Must include:
- Sequence
- Selection
    - Selection must include Logical Operators
- A collection data structure appropriate for the task
- Files Operations (Reading from and writing to text files)
- the use of string manipulation to modify text
    - This can include string concatenation and formatting strings
- A mathematic Operation.
- Add contact and save contact are to be different
- adding a contact adds the contact to a list
- Saving a contact then adds the list to the file.
- Phone number needs to be numeric and 10 digits
- Viewing contacts displays contact information from the file.
- Delete removed contacts from the file
- use functions for add, view, delete, and save

- Needs header commends
- at least one library function

READ ALGORITHM
- Open File in read mode
- Read each line sequentially until the end of the file is reached
Process each line as it is read

WRITE ALGORITHM
- Open the file in write mode (overwriting any existing content)
- Write each line sequentially to the file.

'''

'''
#PSEUDOCODE:
START
## Create contacts file
IF file "contacts.txt" does not exist
CREATE "contacts.txt"
SET <contacts_path> to location of "contacts.txt"

## Define Functions

DEFINE FUNCTION <func_delete> WITH PARAMETERS
    OUTPUT "Enter Contact ID"
    WRITE "contacts.txt" removing data with ID from USERINPUT
DEFINE FUNCTION <func_add> WITH PARAMETERS

DEFINE FUNCTION <func_save> WITH PARAMETERS <newcontacts>
    WRITE "contacts.txt" appending <contacts_list>
## select user actions
SET <selection> to ""
SET <contacts_list> to ""

WHILE <selection> is not "exit"
OUTPUT "Select: [1] View, [2] Delete, [3] Add, [4] Save, [5] exit"
SET <selection> to USERINPUT

IF <selection> is "1" THEN
    IF file "contacts.txt" exists
        READ "contacts.txt"
    ELSE
        OUTPUT "There are no Contacts to View "
ELIF <selection> is "2" THEN
    CALL <func_delete>
ELIF <selection> is "3" THEN
    CALL <func_add>
ELIF <selection> is "4" THEN
    CALL <func_save>
ELIF <selection> is "5" THEN
    OUTPUT "are you sure? any unsaved data will be lost [Y/N]"
    IF USERINPUT is "Y"
        SET <selection> to "exit"
    ELSE
        OUTPUT "cancelling Exit"
ELSE
    OUTPUT "Invalid Selection"


'''
## Setting up working directory, making sure it is always placed relative to the script file.
import os
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles"):
    os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles")
current_dir = os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles"
print("Files are stored at: " + current_dir + "")

print("Welcome to Project A, the Simple Contacts Application!")

# DEFINING VARIABLES
## Creating the Contacts file relative to the activation script
## regardless of if run in debug or from terminal

contacts_list = ""
contacts_path = os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles/Contacts.txt"
contacts_heading = ["contact_id", "first_name", "last_name", "ph_num", "email", "category"]
if not os.path.exists(contacts_path):
    with open(current_dir + "/Contacts.txt","w+") as text_data:
        text_data.write(str(contacts_heading))

# CREATING DEFS
## MAJOR FUNCTIONS
### Add Contacts Function
#### For creating a new contact and adding it to the contacts_list variable
def add_func(contact):
    first_name = input("first name: ")
    last_name = input("last name: ")
    
    # user inputs a number that has to be 10 digits, or leave blank despite better judgement
    # Credit heinst on stackoverflow for some of this one
    ph_num = input("Phone Number (in 10 digits): ")
    ph_num = ph_num.replace(" ","") # for people who write 0400 000 000 instead of 0400000000
    if ph_num == "":
        print("It is weird to add a contact without a contact number.\npress enter again to confirm this is what you want to do [enter]")
    while len(ph_num) != 10 or (not ph_num.isdigit()): # will keep going until answer is 10 digits or blank
        print("not a correct format")
        ph_num = input("Phone Number (in 10 digits): ")
        if ph_num == "":
            break
    
    email = input("Email: ")

    # Tag system, with stub to leave room for adding custom tags feature in the future
    category = input("Tag this contact as\n[1] Friend \n[2] Family: ")
    if selection_func("Friend","1",category) == "1":
        print("Contact saved as a friend\n")
    elif selection_func("custom","2",category) == "2":
        print("Contact saved as family\n")
    elif selection_func("custom","0",category) == "0":
        category = ""
        print("Custom tag feature coming soon!")
    elif category == "":
        print("Saved without a category")
    else:
        category = ""
        print("unrecognised tag, if only we can make custom tags! ")
    
    # Confirm contact details and append to list
    if category == "":
        confirm_contact = input(f"Confirm this contacts details:\nName: {first_name} {last_name}\nPhone Number: {ph_num}\nEmail: {email}\nuncategorised\n[1] YES\n[2] NO\n ")
    else:
        confirm_contact = input(f"Confirm this contacts details:\nName: {first_name} {last_name}\nPhone Number: {ph_num}\nEmail: {email}\nplaced in the {category} group\n[1] YES\n[2] NO\n ")
    while confirm_contact != "1":
        if selection_func("Yes", "1", confirm_contact) == "1": 
            confirm_contact = "1"
            contact = "test"
            return contact

            print("Contact added.\nsave to file in main menu\n")

        elif selection_func("No", "2", confirm_contact) == "2": 
            confirm_contact = "2"
            print("Contacts not saved\n")
        else:
            print("unrecognised command\n")
            confirm_contact = input("Confirm Contact? [Yes/No]")

## MINOR FUNCTIONS
### Select Options Function
#### This automatically creates possible user inputs that will select the option
#### Example: if we want to select [1] Add, we can type 1, add, Add, ADD
def selection_func(name, number, var_value):
    if var_value == name or var_value == str.lower(name) or var_value == number or var_value == str.upper(name):
        print("option ",name," selected\n")
        var_value = number
        return var_value
#### 

# Starting menu
selection = "" # Variable that is used to determine the next action
# exit_commands = ["Exit", "Quit", "Kill", "End", "Poweroff"]
while selection != "forcequit" : #sets the program to end if you type forcequit. selection is set to this when you confirm exit
    print("contacts to submit: ", contacts_list)
    selection = input("\n...\nSelect your action\n [1] Add \n [2] Save \n [3] View\n [4] Delete\n [5] Exit \n Answer: ")
    
    # Actions to take depending on user choice

    if selection_func("Add","1",selection) == "1":
        add_func(contacts_list)


    elif selection_func("Save","2",selection) == "2":
        print("Saving function goes here")
        print(contacts_list)
    # Viewing function, COMPLETE                                    #
    elif selection_func("View","3",selection) == "3":               #
        print("Reading data from file ", contacts_path,": \n")      #
        if os.path.exists(contacts_path):                           #
            with open(contacts_path,"r") as text_data:              # 
                for line in text_data:                              #
                    print(line, end="")                             #
        else:                                                       #
            print("ERROR: Can't find contacts file!\n")             #

    elif selection_func("Delete","4",selection) == "4":
        print("Delete function goes here")


    # Various options that allow for quitting the program
    elif selection_func("Exit","5",selection) == "5" or selection_func("Quit","5",selection) == "5" or selection_func("End","5",selection) == "5" or selection_func("Kill","5",selection) == "5":
        selection = input("are you sure you want to Exit?\n Any unsaved data will be lost [Y/N]: ")
        # Allows you to answer with "Yes, Y, y, or repeating the exit command"
        if selection == selection_func("Yes",5,selection) == "5" or selection == "Y" or selection == "y" or selection_func("Exit","5",selection) == "5" or selection_func("Quit","5",selection) == "5" or selection_func("End","5",selection) == "5" or selection_func("Kill","5",selection) == "5":
            print("Quitting\n")
            selection = "forcequit"
        elif selection == selection_func("No",0,selection) == "0" or selection == "N" or selection == "n" or selection_func("Cancel",0,selection) == "0":
            print("Cancelling Exit, reuturning to main menu\n...\n")
        else:
            print("unclear command, returning to main menu\n...\n")
    #for when the user inputs a value that has no programmed response
    else:
        print("Not a recognised command, try again")

    ## Changes value of add_new_contact so it will always be the lowercase first letter of the input
    