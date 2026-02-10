#module - python file that contains python code, it can have functions,variables that you want
# to include it in your file
#import the module
import math as fm
import random
import datetime
print(fm.sqrt(49))
print(fm.pi)
print(fm.floor(6.98))
print(fm.ceil(6.98))
print(fm.degrees(76))
#generate random int between 5-14
print(random.randint(5,14))
#generate random num between 0 and 1
print(random.random())
#generate current time and date
print(datetime.datetime.now().hour)
x=datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
print(x.minute)
