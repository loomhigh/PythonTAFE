'''
## IN CLASS ACTIVITY

# Assinging Sentence a string value
sentence = "This is a Python course"

# grab the desired word in the sentence variable and print it
print(sentence[10:16])
'''
user_date = ""
user_date = input("input current date [DD/MM/YYYY] ")

cal_breakfast = 0
cal_lunch = 0
cal_dinner = 0

cal_breakfast = float(input("hinput breakfast calories "))
cal_lunch = float(input("hinput lunch calories "))
cal_dinner = float(input("hinput dinner calories "))

sum_calories = 0
sum_calories = cal_breakfast + cal_lunch + cal_dinner

print("on day",user_date[0:2],"of month",user_date[3:5], "in the year of",user_date[6:10],", you ate",sum_calories, "calories of food!")