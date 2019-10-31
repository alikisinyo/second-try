# a group of code perfoming a specified task
# def function name():
#             staements
# example 1
# def sayhi():
#     print("hello world")
#
#
# sayhi()
# example 2
def add(a, b):
    # summ = a + b
    # print(summ)
    print(a + b)


add(2, 3)


def subtract(a, b):
    # summ = a - b
    # print(summ)
    print(a - b)


subtract(2, 3)


def divide(a, b):
    # summ = a / b
    # print(summ)
    print(a / b)


divide(2, 3)


def multiply(a, b):
    # summ = a * b
    # print(summ)
    print(a * b)


multiply(2, 3)


def checker(a):
    if a > 100:
        print("number is greater than 100")
    elif a == 100:
        print("number is equal to 100")
    else:
        print("number is less than 100")


checker(90)


def divisor(a):
    print(a % 2)


divisor(6)


#
# def firstCapital(name):
#     name = input("Enter you name: ")
#     print(name.capitalize())
#
#
# firstCapital("ali")
#
#
def upperCase(name):
    index1 = name[0].upper
    fullname = index1 + name[1:]
    print(fullname)


upperCase(name)
#
# def name(aName):
#     print(aName.replace("morning", "afternoon"))


# def subtract(a, b):
#     # summ = a - b
#     # print(summ)
#     return a - b
#
#
# print(subtract(10, 10))
