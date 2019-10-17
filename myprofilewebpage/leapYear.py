name = input("What is your Name? ")
print("Hello " + name)
year = input("What is your birth year? ")
year = eval(year)
print(year)
if year % 4 == 0:
    print("That is a Leap year!! ")
else:
    print("Thats not a leap year " + name)
age = 2019 - year
age = str(age)

print("By the way " + name + ", you are " + age + " yrs old")
