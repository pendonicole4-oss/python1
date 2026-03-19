#inheritance - a child inherits attributes and methods from a parent
#super/parent class
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'The animal, {self.name}, is {self.age} years old'

    def speak(self):
        return f"Hello"
    def supermethod(self):
        return f"Hello from a method in superclass"

#child/subclass
class Dog(Animal):
    def speak(self):
        return "Bark bark"
    def chrome(self):
        return f'Hello from a method in dog class'

#child2
class Cat(Animal):
    def speak(self):
        return "Meow meow"
    def moxilla(self):
        return 'Hello from a  method in cat class'

#create a dog object
mydog=Dog("Bob",5)
print(mydog.name)
#call a parent method
print(mydog.supermethod())
#overidding method
print(mydog.speak())
#calling our own method
print(mydog.chrome())

#create a cat object
cat1=Cat("Pinky",3)
cat2=Cat("Becky",10)
print(cat1)
print(cat2)
#call the speak method
print(cat2.speak())
