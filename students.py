#class is a blueprint for creating objects
#object is a vinsance of a class
from unicodedata import name


class Student:
    #constructor
    #runs automatically when an object is created
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def __str__(self):
        return f"The student name: {self.name} , Age: {self.age} and Course : {self.course}"
    def get_email(self):
        return f'{self.name}.emobilis.ac.ke'
#create an object
#object is an instance of a class
#objectname=classname(values)
student1=Student("Pendo",18,"MIT")
student2=Student("Imani",17,"AI")
print(student1)
print(student2)
#callin' our function
print(student1.get_email())
print(student2.get_email())


