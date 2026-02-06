#list= used to store multiples elements in a single variable
#list is ordered,change and allows duplicates
from icu import UAlphabeticIndexLabelType

students=["Nicole","Angela","Kyle","Jay","Lydia"]
mynums=[53,74,85,35,37,78]
print(students)
print(mynums)
print(type(students))
print(type(mynums))
#len()- length
print(len(students))
print(len(mynums))
#accessing list items
print(students[0])
print(students[2])
print(mynums[3])
#modifying list items
print(students)
students[1]="Gichuru"
print(students)
#list methods, append(),remove(),pop()
#append- adds an item at the end
students.append("Leilani")
print(students)
#remove - removes a specific item
students.remove("Jay")
print(students)
#insert() - adds an element at a specific index
students.insert(1,"Pendo")
print(students)
#looping through a list
for x in students:
    print(x)
course=["Fullstack","Data Science","Cyber Security",]
print(course)
course.insert(1,"AI")
print(course)
course.remove()

