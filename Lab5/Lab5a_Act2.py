# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do"
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: William Roberts 530008478
#       Brandon White   331004571
#       Huy Laz         132000354
#       John Rios Jr.   631004090
# Section:    469-569
# Assignment: Lab5a Activity 2
# Date:       9/28/2021
#

#Determine inputs
sex = input("Enter your sex (M/F): ").lower()
age = int(input("Enter your age (years): "))
smoker = input("Do you smoke cigarettes (Y/N)? ").lower()
t_c = int(input("Enter your total cholesterol (mg/dL): "))
HDL_c = int(input("Enter your HDL cholesterol (mg/dL): "))
s_BP = int(input("Enter your systolic BP (mmHg): "))
med = input("Are you taking blood pressure medication (Y/N)? ").lower()

points = 0   #Start with 0 and add along the way

#For males
if sex == "m":
    #Age and age bassed variables
    if age < 20:
        print ("your young, why are you worried about heart attacks")
    elif age < 35:
        points -= 9
        if smoker == "y":         #Smoke variable
            points += 8
        if t_c < 160:             #total Blood pressure
            points += 0
        elif t_c < 200:
            points += 4
        elif t_c < 240:
            points += 7
        elif t_c < 280:
            points += 9
        elif t_c >= 280:
            points += 11
    elif age < 40 :
        points -= 4
        if smoker == "y":
            points += 8
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 4
        elif t_c < 240:
            points += 7
        elif t_c < 280:
            points += 9
        elif t_c >= 280:
            points += 11
    elif age < 45:
        points += 0
        if smoker == "y":
            points += 5
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 3
        elif t_c < 240:
            points += 5
        elif t_c < 280:
            points += 6
        elif t_c >= 280:
            points += 8
    elif age < 50:
        points += 3
        if smoker == "y":
            points += 5
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 3
        elif t_c < 240:
            points += 5
        elif t_c < 280:
            points += 6
        elif t_c >= 280:
            points += 8
    elif age < 55:
        points += 6
        if smoker == "y":
            points += 3
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 2
        elif t_c < 240:
            points += 3
        elif t_c < 280:
            points += 4
        elif t_c >= 280:
            points += 5
    elif age < 60:
        points += 8
        if smoker == "y":
            points += 3
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 2
        elif t_c < 240:
            points += 3
        elif t_c < 280:
            points += 4
        elif t_c >= 280:
            points += 5
    elif age < 65:
        points += 10 
        if smoker == "y":
            points += 1
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 1
        elif t_c < 240:
            points += 1
        elif t_c < 280:
            points += 2
        elif t_c >= 280:
            points += 3
    elif age < 70:
        points += 11
        if smoker == "y":
            points += 1
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 1
        elif t_c < 240:
            points += 1
        elif t_c < 280:
            points += 2
        elif t_c >= 280:
            points += 3
    elif age < 75:
        points += 12
        if smoker == "y":
            points += 1
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 0
        elif t_c < 240:
            points += 0
        elif t_c < 280:
            points += 1
        elif t_c >= 280:
            points += 1
    elif age < 80:
        points += 13
        if smoker == "y":
            points += 1
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 0
        elif t_c < 240:
            points += 0
        elif t_c < 280:
            points += 1
        elif t_c >= 280:
            points += 1
   
    if HDL_c < 40:
        points += 2
    elif HDL_c < 50:
        points += 1
    elif HDL_c < 60:
        points += 0
    elif HDL_c >= 60:
        points -= 1
    
    if s_BP < 120:
        points += 0
    elif s_BP < 130:
        if med == "y":
            points += 1
        else:
            points += 0
    elif s_BP < 160 :
        if med == "y":
            points += 2
        else:
            points += 1
    elif s_BP >= 160 :
        if med == "y":
            points += 3
        else:
            points += 2
    
    if points < 0:
        risk = "<1"
    elif points < 5:
        risk = 1
    elif points < 7:
        risk = 2
    elif points == 7:
        risk = 3
    elif points == 8:
        risk = 4
    elif points == 9:
        risk = 5
    elif points == 10:
        risk = 6
    elif points == 11:
        risk = 8
    elif points == 12:
        risk = 10
    elif points == 13:
        risk = 12
    elif points == 14:
        risk = 16
    elif points == 15:
        risk = 20
    elif points == 16:
        risk = 25
    elif points >= 17:
        risk = ">30"
        
        
else:
    #For women
    #Age and age bassed variables
    if age < 20:
        print ("your young, why are you worried about heart attacks")
    elif age < 35:
        points -= 7
        if smoker == "y":         #Smoke variable
            points += 9
        if t_c < 160:             #total Blood pressure
            points += 0
        elif t_c < 200:
            points += 4
        elif t_c < 240:
            points += 8
        elif t_c < 280:
            points += 11
        elif t_c >= 280:
            points += 13
    elif age < 40 :
        points -= 3
        if smoker == "y":
            points += 9
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 4
        elif t_c < 240:
            points += 8
        elif t_c < 280:
            points += 11
        elif t_c >= 280:
            points += 13
    elif age < 45:
        points += 0
        if smoker == "y":
            points += 7
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 3
        elif t_c < 240:
            points += 6
        elif t_c < 280:
            points += 8
        elif t_c >= 280:
            points += 10
    elif age < 50:
        points += 3
        if smoker == "y":
            points += 7
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 3
        elif t_c < 240:
            points += 6
        elif t_c < 280:
            points += 8
        elif t_c >= 280:
            points += 10
    elif age < 55:
        points += 6
        if smoker == "y":
            points += 4
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 2
        elif t_c < 240:
            points += 4
        elif t_c < 280:
            points += 5
        elif t_c >= 280:
            points += 7
    elif age < 60:
        points += 8
        if smoker == "y":
            points += 4
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 2
        elif t_c < 240:
            points += 4
        elif t_c < 280:
            points += 5
        elif t_c >= 280:
            points += 7
    elif age < 65:
        points += 10 
        if smoker == "y":
            points += 2
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 1
        elif t_c < 240:
            points += 2
        elif t_c < 280:
            points += 3
        elif t_c >= 280:
            points += 4
    elif age < 70:
        points += 12
        if smoker == "y":
            points += 2
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 1
        elif t_c < 240:
            points += 2
        elif t_c < 280:
            points += 3
        elif t_c >= 280:
            points += 4
    elif age < 75:
        points += 14
        if smoker == "y":
            points += 1
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 1
        elif t_c < 240:
            points += 1
        elif t_c < 280:
            points += 2
        elif t_c >= 280:
            points += 2
    elif age < 80:
        points += 16
        if smoker == "y":
            points += 1
        if t_c < 160:
            points += 0
        elif t_c < 200:
            points += 1
        elif t_c < 240:
            points += 1
        elif t_c < 280:
            points += 2
        elif t_c >= 280:
            points += 2
            
    if HDL_c < 40:
        points += 2
    elif HDL_c < 50:
        points += 1
    elif HDL_c < 60:
        points += 0
    elif HDL_c >= 60:
        points -= 1
        
    if s_BP < 120:
        points += 0
    elif s_BP < 130:
        if med == "y":
            points += 3
        else:
            points += 1
    elif s_BP < 140:
        if med == "y":
            points += 4
        else: 
            points += 2
    elif s_BP < 160 :
        if med == "y":
            points += 5
        else:
            points += 3
    elif s_BP >= 160 :
        if med == "y":
            points += 6
        else:
            points += 4
    
    if points < 9:
        risk = "<1"
    elif points < 12:
        risk = 1
    elif points < 15:
        risk = 2
    elif points == 15:
        risk = 3
    elif points == 16:
        risk = 4
    elif points == 17:
        risk = 5
    elif points == 18:
        risk = 6
    elif points == 19:
        risk = 8
    elif points == 20:
        risk = 11
    elif points == 21:
        risk = 14
    elif points == 22:
        risk = 17
    elif points == 23:
        risk = 22
    elif points == 24:
        risk = 27
    elif points >= 25:
        risk = ">30"
        
        
print ("Your 10-year risk of a heart attack is {}%".format(risk))