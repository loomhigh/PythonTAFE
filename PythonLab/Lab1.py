
'''
Author: Wyatt Teakle
'''

print("Welcome to Lab1")

#'''
#Session 5 Activity Code page 10

# Find and record the absolute path of current blank file IO program
newmail = "y"
while newmail == "y":
    with open("/home/personal/Python/PythonTAFE/PythonLab/Topic5/Contacts.txt","a") as mytext:
        new_mail = input("add to the mailing list: ")
        mytext.write("\n" + new_mail)
    newmail = input ("Would you like to add another? (Y/N) ")
    newmail = str.lower(newmail[0])

with open("/home/personal/Python/PythonTAFE/PythonLab/Topic5/Contacts.txt", "r") as mytext:
    for line in mytext:
        print(line, end="")






#'''