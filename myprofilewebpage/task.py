# Task
taskList = [23, "Jane", ["Lesson 23", 560, {"currency":"KES"}], 987, (76,"John")]
# 1. determine the type of variable in taskList using an inbuilt function
# 2. Print KES from taskList
# 3. print 560 from taskList
# 4. Use a function to determine the length of the taskList
# 5. Change 987 to 789 without using an inbuilt method or assigment
# 6. change name "John" to "Jane" without using assignment
print (type(taskList))
print (taskList[2][2]["currency"])
print (taskList[2][1])
print (len(taskList))
# convert it to a string since integers cannot be reversed in their current for
print(str(taskList[3])[::-1])
# 6 tuples cannot be changed they are immutable



