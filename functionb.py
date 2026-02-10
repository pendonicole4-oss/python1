#function with return keyword return a keyword
from pyparsing import conditionAsParseAction
def addThreeNumbers(e,f,g):
    sum=e+f+g
    print("The sum is",sum)

addThreeNumbers(7,8,4)


#functions that adds two numbers
def addTwoNumbers(a,b):
    sum=a+b
    return sum
#calling the function and storing the returned value in a variable
result=addTwoNumbers(18,86)
print("The sum is",result)
#way 2
print(addTwoNumbers(764,986))

#function that multiplies 3 numbers
def multiply3Numbers(x,y,z):
    multiplication=x*y*z
    return multiplication
#calling the function
multiply=multiply3Numbers(65,64,36)
print("The multiplication is",multiply)


#function that checks if a number is even or odd
def odd_even(c):
    if c%2==0:
        print(c, " is an even number")
    else:
        print(c, "is an odd number")
# get user input
num=int(input("Enter a number to check if number is even or odd "))
#calling
odd_even(num)


#function that finds maximum of two numbers
def maximum(x,y):
    return max(x,y)
number=maximum(64,84)
print(f"The maximum number is {number}")




