
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
    OUTPUT "what is their name?"
    Set <contact_name> to USERINPUT
    OUTPUT "What is their number?"
    set <contact_number> to USERINPUT
    OUTPUT "what is their email?"
    set <contact_email> to USERINPUT
    OUTPUT "are they a friend or family?"
    set <contact_tag> to USERINPUT
    PRINT "The following contact has been created"
    set <contact_details> to list of <contact_name>,<contact_number>,<contact_email>,<contact_tag>
    PRINT <contact_details>
    OUTPUT "Would you like to save the contact?"
    if USERINPUT is "Yes" THEN
        set <user_id> to 1 plus number of contacts in "contacts.txt"
        set <new_contact> to list containing 6 items from <user_id>,<contact_name>,<contact_number>,<contact_email>,<contact_tag>
    if USERINPUT is "No" THEN
        BREAK
DEFINE FUNCTION <func_save> WITH PARAMETERS <newcontacts>
    WRITE "contacts.txt" appending <contacts_list>
## select user actions
SET <selection> to ""
SET <contacts_list> to ""

WHILE <selection> is not "exit"
OUTPUT "Select: [1] View, [2] Delete, [3] Add, [4] Save, [5] exit"
SET <selection> to USERINPUT

IF <selection> is "1" or "View" THEN
    IF file "contacts.txt" exists
        READ "contacts.txt"
    ELSE
        OUTPUT "There are no Contacts to View "
ELIF <selection> is "2" or "Delete" THEN
    CALL <func_delete>
ELIF <selection> is "3" or "Add" THEN
    set <contacts_list> to <contacts_list> and <new_contact> in CALL <func_add>

ELIF <selection> is "4" or "Save" THEN
    CALL <func_save>
ELIF <selection> is "5" or "Exit" THEN
    OUTPUT "are you sure? any unsaved data will be lost [Y/N]"
    IF USERINPUT is "Y"
        EXIT program
    ELSE
        OUTPUT "cancelling Exit"
ELSE
    OUTPUT "Invalid Selection"


'''
## Setting up working directory, making sure it is always placed relative to the script file.
import os #used for ensuring correct directory structure
import time #adding sleep command. Purely aesthetic
import datetime #used for creating IDs
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles"):
    os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles")
current_dir = os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles"
print("Files are stored at: " + current_dir + "")

print("Welcome to Project A, the Simple Contacts Application!")

# DEFINING VARIABLES
## Creating the Contacts file relative to the activation script
## regardless of if run in debug or from terminal

contacts_list = []
contacts_path = os.path.dirname(os.path.realpath(__file__)) + "/ProjectFiles/Contacts.txt"
contacts_heading = ["contact_id", "first_name", "last_name", "ph_num", "email", "category"]
if not os.path.exists(contacts_path):
    with open(current_dir + "/Contacts.txt","w+") as text_data:
        text_data.write("")

# CREATING DEFS
## MAJOR FUNCTIONS
### Add Contacts Function
#### For creating a new contact and adding it to the contacts_list variable
def add_func():
    '''
    Local Vars:
        newcontact_ID: date and time down to the second used as a unique ID
        first_name: First name of the contact
        last_name:  Last name of the contact
        ph_num:     Phone number of the contact, must be either 10 digits or blank. All spaces will automatically be removed
        email:      Contacts Email Address. no special rules, just a string.
        category:   Option of tagging the contact as either friend, family, or left blank
        new_contact: List containing contact details of newly inputted contact
    '''
    timestamp = datetime.datetime.now()
    newcontact_id = timestamp.strftime("%y%m%d%H%M%S") #creates unique newcontact ID
    first_name = input("first name: ")
    last_name = input("last name: ")
    
    # user inputs a number that has to be 10 digits, or leave blank despite better judgement
    # Credit heinst's suggestions on stackoverflow for some of this one
    ph_num = input("Phone Number (in 10 digits): ")
    ph_num = ph_num.replace(" ","") # for people who write 0400 000 000 instead of 0400000000
    if ph_num == "":
        print("it is inadvisable to add a contact without a contact number.\npress enter again to confirm this is what you want to do [enter]")
    while len(ph_num) != 10 or (not ph_num.isdigit()): # will keep going until answer is 10 digits or blank
        print("not a correct format")
        ph_num = input("Phone Number (in 10 digits): ")
        ph_num = ph_num.replace(" ","")
        if ph_num == "":
            break
    
    email = input("Email: ")

    # Tag system, with stub to leave room for adding custom tags feature in the future
    category = input("Tag this contact as\n[1] Friend \n[2] Family: ")
    #while category != "1" or category != "2":
    if selection_func("Friend","1",category) == "1":
        category = "1"
        print("Contact saved as a friend\n")
    elif selection_func("custom","2",category) == "2":
        category = "2"
        print("Contact saved as family\n")
    elif selection_func("custom","0",category) == "0":
        category = ""
        print("Custom tag feature coming soon!\n")
        category = input("Tag this contact as\n[1] Friend \n[2] Family: ")
    elif category == "":
        print("You Need to select a category\n")
        category = input("Tag this contact as\n[1] Friend \n[2] Family: ")
    else:
        category = ""
        print("unrecognised tag, if only we can make custom tags! ")
        category = input("Tag this contact as\n[1] Friend \n[2] Family: ")
    
    # Confirm contact details and append to list

    if category == "": 
        # confirm_contact = input(f"Confirm this contacts details:\nName: {first_name} {last_name}\nPhone Number: {ph_num}\nEmail: {email}\nuncategorised\n[1] YES\n[2] NO\n ")
        print("No category selected")
        contact = None
        return contact 
        confirm_contact = "2"
    else:
        confirm_contact = input(f"Confirm this contacts details:\nName: {first_name} {last_name}\nPhone Number: {ph_num}\nEmail: {email}\nplaced in group {category}\n[1] YES\n[2] NO\n ")
    while confirm_contact is not True:
        if selection_func("Yes", "1", confirm_contact) == "1": 
            contact = [newcontact_id,first_name,last_name,ph_num,email,category]   # sets contact to the contact details
            return contact                                              # Returns to global variable, contactsr_list
            print("Contact added.\nsave to file in main menu\n")        # Informs user that contact was added to Var
            confirm_contact = True                                      # sets confirm_contact to true, breaking while loop
        elif selection_func("No", "2", confirm_contact) == "2":         
            confirm_contact = "2"                                       # sets confirm_contact to 2, which means no
            print("Contact cancelled\n")                                # Informs user that the contact won't be saved
            contact = None
            return contact 
            break                                                       # sets confirm_contact to true, breaking while loop
        else:
            print(f"command {confirm_contact} not recognised\n")        # relays incorrect command for user to correct
            contact = None
            return contact 
            #confirm_contact = input("Confirm Contact? [Yes/No]")        # Asks again

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
while selection != "forcequit" : #sets the program to end if you type forcequit.
    if len(contacts_list) > 0:
        print("\n",len(contacts_list), "contacts to submit: ", [row[1] for row in contacts_list])  
        selection = input("\n...\nSelect your action\n [1] Add \n [2] Save \n [3] View\n [4] Delete\n [5] Exit \n Answer: ")         #
    else:                                                                                                                            #
        print("\n no contacts are ready to submit")                                                                                               #  
        selection = input("\n...\nSelect your action\n [1] Add \n [2] Save \n [3] View\n [4] Delete\n [5] Exit \n Answer: ")         #
    # Actions to take depending on user choice

    # Add function COMPLETE
    if selection_func("Add","1",selection) == "1":
        adding_new_contact = []
        adding_new_contact = [add_func()]
        if adding_new_contact != [None]:
            contacts_list += adding_new_contact #Adds returned function to contracts list list.
        else:
            print("no valid contact added, reverting to main menu\n")

    # Saving function COMPLETE
    elif selection_func("Save","2",selection) == "2":
        # Viewng Submission
        print("The following will be saved to",contacts_path,":")
        time.sleep(0.2)
        print(contacts_heading)
        for row in contacts_list:
            time.sleep(0.2) # Give the user time to comprehend that the list has been displayed
            print(row, end="\n")
        # / Viewing submission

        # Save command
        selection = input("\n Are you Sure you want to save? \nSelect your action\n [1] Yes \n [2] No\n")
        if selection_func("Yes", "1", selection) == "1": 
            if os.path.exists(contacts_path): 
                print("Saving...\n")
                with open(contacts_path,"a") as newdata:
                    for items in contacts_list:
                        newdata.write("%s\n" % items)
                #newdata.write(contacts_list) #writes contacts_list variable to contacts file
                contacts_list = [] # Clears contacts_list variable.
            else:
                print("ERROR: Contacts file not found. Restart program to fix!\n")

        elif selection_func("No", "2", selection) == "2": 
            print("Cancelling...\n")
        else:
            print("unclear command.")
        
        #/ Save command

    # Viewing function, COMPLETE                                    #
    elif selection_func("View","3",selection) == "3":               #
        print("Reading data from file ", contacts_path,": \n")      #
        if os.path.exists(contacts_path):               
            print(contacts_heading)
            contact_read = []
            with open(contacts_path,"r") as text_data:
                for element in text_data:
                    contact_read += [element]
                #contact_read = text_data.read().splitlines()            # 
                for line in contact_read:    
                    time.sleep(0.2)                            
                    print(line, end="")
                print(len(contact_read), "total contacts")            
                input("press enter to return to menu")
        else:                                                       #
            print("ERROR: Can't find contacts file!\n")  
                    
    # Delete function
       
    elif selection_func("Delete","4",selection) == "4":
        # Bring up contacts to delete
        snuffed_person = ""
        delete_contact = ""
        print("[_____ID_____] - First  Last\n[1]            - Cancel    Action")
        if os.path.exists(contacts_path):                           #
            contact_read = []
            with open(contacts_path,"r") as text_data:              # 
                for element in text_data:
                    contact_read += [element]
                #contact_read = text_data.read().splitlines()
                while len(delete_contact) != 12 or (not delete_contact.isdigit()):
                    for element in contact_read:
                        time.sleep(0.2)
                        print(("[" + element.split()[0].replace("[","") + "] - " + element.split()[1] + "   " + element.split()[2]).replace("'","").replace(",",""))
                    delete_contact = input("\nSelect UID\n")
                    if selection_func("Exit","1",delete_contact) == "1" or selection_func("Quit","5",delete_contact) == "5" or selection_func("End","1",delete_contact) == "1" or selection_func("Kill","1",delete_contact) == "1":
                        delete_contact = "000000000000"
                    elif not delete_contact.isdigit():
                        print("not a valid number, try again:")
                    elif len(delete_contact) != 12:
                        print("Contact UID should be 12 digits, try again:")

        # Delete Selection
        for element in contact_read:
            if element.split()[0].replace("['","").replace("',","") == delete_contact:
                snuffed_person = element
            else:
                print("...")
                time.sleep(0.1)
        # Deleting For real
        if snuffed_person != "":
            contact_read.pop(contact_read.index(snuffed_person))      # Deletes input contact from variable
            if os.path.exists(contacts_path):                           #
                with open(contacts_path,"w") as text_data:              # 
                    for line in contact_read:                           # 
                        text_data.write(line)                  #  
            

    # Various options that allow for quitting the program

    elif selection_func("Exit","5",selection) == "5" or selection_func("Quit","5",selection) == "5" or selection_func("End","5",selection) == "5" or selection_func("Kill","5",selection) == "5":
        selection = input("are you sure you want to Exit?\n Any unsaved data will be lost [Y/N]: ")
        # Allows you to answer with "Yes, Y, y, or repeating the exit command"
        if selection == selection_func("Yes",5,selection) == "5" or selection == "Y" or selection == "y" or selection_func("Exit","5",selection) == "5" or selection_func("Quit","5",selection) == "5" or selection_func("End","5",selection) == "5" or selection_func("Kill","5",selection) == "5":
            print("Quitting\n")
            selection = "forcequit"
        elif selection == selection_func("No",0,selection) == "0" or selection == "N" or selection == "n" or selection_func("Cancel",0,selection) == "0":
            print("Returning to main menu\n...\n")
        else:
            print("unclear command, returning to main menu\n...\n")
    
    #for when the user inputs a value that has no programmed response
    else:
        if selection == "forcequit": #instantly closes progrm
            print("\nForce Quitting... ")
        elif selection == "restart": #Restarts the script, useful if save file deleted mid-run
            os.execv(sys.argv[0], sys.argv)
        else:
            print("Not a recognised command, try again")
            time.sleep(0.5)

    ## Changes value of add_new_contact so it will always be the lowercase first letter of the input
    