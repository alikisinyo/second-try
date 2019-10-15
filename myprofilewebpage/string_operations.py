# concatinating is joining two strings
# using +

firstName = "Ali"
lastName = "Kisinyo"

fullName = firstName + " " + lastName
print (fullName)

# format
fullName = "{} {}".format(firstName, lastName)
print (fullName)

print ("the shortest name in history is {} from the digo clan son of {}".format(firstName, lastName))

names = "juma boy"
name2 = "ALI ABDALLAH"
name3 = "Mohamed Kisinyo"

print (name2.title())

sen = "man is to error because man did not create Man"
print (sen.lower().count(" "))
# python is case sensitive


# string slicing
# left of the colon signifies the starting element
# right of the colon signifies the ending position but that element is excluded

sen = "man is to error because man did not create Man"
print (sen[0:3])

# print string reverse
jina = "muyani"
print (jina[::-1])

# spliting
# can be used to clean data
print (sen.split("a"))

