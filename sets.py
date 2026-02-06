#sets  - are unordered,unchangeable and do not allow duplicates
rooms={"Chrome","Moxilla","Firefox","Brave","Safari"}
print(rooms)
print(type(rooms))
#len()
print(len(rooms))
for x in rooms:
    print(x)
#remove
rooms.remove("Brave")
print(rooms)
#add
rooms.add("Opera")
print(rooms)

