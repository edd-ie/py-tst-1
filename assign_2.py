import string

taskList = [23, "Jane", ["Lesson 23", 560, {"currency": "KES"}], 987, (76, "John")]

print(type(taskList))  # Task 1: determine data type

y = taskList[2]
print(y[2]["currency"])
print(taskList[2][2]["currency"])  # Task 2: print KES

print(taskList[2][1])  # Task 3: print 560

print(len(taskList))  # Task 4: Length of task_list

m = taskList[3]
n = str(m)[::-1]  # first convert the number to a string by str(..)
print(n)
print(str(taskList[3])[::-1])  # Task 5: change 987 to 789

m = taskList[4][1]  # first identify the value
print(m.replace("John", "Jane"))  # input the var.replace(old, new)
print(taskList[4][1].replace("John", "Jane"))  # Task 5: change John to Jane





