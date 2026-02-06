#elif - used to test different conditions
"""
if..elif..else
if condition1:
     block of code to be executed if condition1 is true
elif condition2:
     block of code to be executed if condition2 is true:
else:
     block of code to be executed if all conditions are false
"""
#a program that asks user for marks then prints the grade
#80-100 A
#70-80 B
#60-70 C
#50-60 D
#else FAIL
marks=int(input("Enter your marks"))
if marks>=80 and marks<=100:
    print("Grade A")
elif marks>=70 and marks<80:
    print("Grade B")
elif marks>=60 and marks<70:
    print("Grade C")
elif marks>=50 and marks<60:
    print("Grade D")
else:
    print("FAIL")
#a program that asks user age and prints
#18-30 young adult
#30-45 adult
#45-65 mature adult
#65-100 elderly
#<18 baby
user_age=int(input("Enter your age"))
if user_age>=18 and user_age<=30:
    print("You are a young adult")
elif user_age>30 and user_age<=45:
    print("You are an adult")
elif user_age>45 and user_age<=65:
    print("You are a mature adult")
elif user_age>65 and user_age<=100:
    print("You are elderly")
elif user_age>100:
    print("You are ancient")
else:
    print("You are a baby!")

