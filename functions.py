#functions - perform a specific task
"""
def functionname():
    block of code
"""
def demo():
    print("Hello, Good afternoon")
#calling the function
demo()
demo()
# another function with parameter
def greetings(name):
    print("Hello",name)
#calling the function
greetings("Nicole")
greetings("Pendo")
#a function with multiple parameters
def student_info(first_name , age=18):
    print(f"Hello {first_name}, you are {age} years old.")
#calling the function
student_info("Nicole",18)
student_info("Kyle")

#functions that calculates area of a rectangle
def areaOfRectangle(l,w):
    area=l*w
    print(f"The area of rectangle with length {l} and width {w} is {area}")
#calling the function
areaOfRectangle(70,40)

#a function that calculates the area of a circle
def areaOfCircle(radius):
    area=3.14*radius*radius
    print(f"The area of a circle with radius {radius} cm is {area}")
#calling the function
areaOfCircle(15)
areaOfCircle(7)

