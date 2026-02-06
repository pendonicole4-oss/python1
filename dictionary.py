#dictionary - stores data in key:value pairs
students={
    "Name":"Nicole",
    "Age":18,
     "Course":"MIT"
}
print(students)
print(type(students))
#accessing the values
print(students["Name"])
print(students["Course"])
print(students["Age"])
 #adding key:value
students["City"]="Nairobi"
print(students)
#updating a value
students["Course"]="Cyber security"
print(students)
#accessing all keys.keys()
print(students.keys())
#values()
print(students.values())
#items
print(students.items())
#loop through all the keys
for x in students.keys():
    print(x)
#loop through all the values
for y in students.values():
    print(y)
#loop through all the items
for x,y in students.items():
    print(x, ":" ,y)


