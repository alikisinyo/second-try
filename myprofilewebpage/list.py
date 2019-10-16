# list is a collection of more than one variable
personalDetails = ["Ali", 15, "Mombasa", True, 3.2]
print (len(personalDetails))

listStudents = ["Eugene", "Kuria", "Ali"]
print (listStudents)
# picking a student from a list
print (listStudents[0])
# spliting
print (listStudents[0:1])
# adding a new student
newStudents = ["Johnston"]
allStudents = listStudents + newStudents
print (allStudents)
# alternative
allStudents.append("Geoffrey")
print (allStudents)
# count specifies the number of items in a list i.e how many times it appear.
print (allStudents.count("Geoffrey"))
# index
pos = allStudents.index("Kuria")
print(pos)
print (allStudents[2:4])
allStudents.insert(0,"Ramadhan")
print (allStudents)
