#tuples are ordered, unchangeable and allow duplicates
course=("HTML","CSS","Python","Bootstrap")
print(course)
print(type(course))
#accessing the item
print(course[1])
#len
print(len(course))
#loop
for x in course:
    print(x)
#tuple()
digits=tuple((43,56,75,46,73,12))
print(digits)
print(type(digits))
for y in digits:
    print(y)
