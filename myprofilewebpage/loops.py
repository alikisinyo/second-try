# sequential programming starts from top to bottom
# condition programming
# iteration programming
# LOOPs
# while loop - repeats execution of its indented block until a specified condition is false
a = 0
# while a < 100:
#     print("Ali Kisinyo")
#     a += 1
#     print(a)
# a format of an ATM PIN format
savedPin = "3333"
tries = 3
attempts = 0
currentPin = input("Please enter you PIN NUMBER: ")
tries -= 1
print("before loop 1")
while currentPin != savedPin and tries > 0:
    currentPin = input("Enter pin ")
    tries -= 1
    print("attempts")
if currentPin != savedPin:
    print("card blocked")
else:
    print("welcome proceed")


