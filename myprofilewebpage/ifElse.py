if True:
    print("True")

marks = input("What you KCPE marks? ")
marks = eval(marks)
name = input("What is your name? ")
if marks < 0 or marks > 500:
    print("Your marks are unrealistic")
else:
    if marks >= 350 and marks <= 500:
        print("congratulations " + name + " you are admitted")
    else:
        print("sorry, Try again")





# read on if -elif-else
