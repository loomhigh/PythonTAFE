
'''
Author: Wyatt Teakle
'''

print("Welcome to Lab3")

#'''
#Session 3 Activity Code

item_name = input("What are you trying to pack? ")
total_items = int(input("how many " + item_name + "(s) do you have? "))
box_cap = int(input("How many " + item_name +  "(s) can fit in one box? "))

box_req = (total_items // box_cap)

#result

print(f"""


"you will need " + {box_req} + " box(es) to store all your" + {item_name} + "(s)"
""")

#'''