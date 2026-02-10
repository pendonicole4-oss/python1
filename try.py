"""
try:
   block of code that can cause error
except:
   #code that runs if error happens
"""
try:
    num=int(input("Enter a number "))
    print(10/num)
except:
    print("You can not divide a number by zero")
#another example
try:
    print(x)
except NameError:
    print("The variable is not defined")

#another example
try:
    with open('abcd.txt','r') as x:
        print(x.read())
except FileNotFoundError:
    print("File not found!")