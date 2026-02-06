#if statement
"""
if-statement specifies a block of code to be executed if condition is true
if condition:
          block of code to be executed if condition is true
"""
x=9
if x<10:
    print(f"{x} is less than 10")
    """if...else
    if condition:
            block of code to be executed if condition is true
else:
     block of code to be executed if condition is false
    """
#a program that checks if a user is eligible to vote
age=12
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
#a program that asks user for age and checks if they can drive
user_age=int(input("Enter your age"))
if user_age>=18:
    print("You can drive")
else:
    print("You cannot drive")
#a program that asks user for a number and checks if the number is even or odd
#hint evennumber%2==0
number= int(input("Enter a number"))
if number%2==0:
    print("That is an even number")
else:
    print("That is an odd number")

#a program that asks for two numbers and prints the greater number
num1=int(input("Enter a first number "))
num2=int(input("Enter a second number"))
if num1>num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

