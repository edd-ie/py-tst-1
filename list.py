# used on changeable data
# uses []

x = ["Eren Jaeger", 19, "Attack Titan", ["potter", "peach"], "3rd wall district", True]  # to create list {var = [0,1,2...], 0-
print(x)
j = x[-1]
print(j)
a = x[3]
print(a[-1])

r = ["Peter piper", "pick a", "bunch of", "pickled peppers", False]  # to create list {var = [0,1,2...]
print(r)
print(type(r))

v = [x, r]
print(v)
print(type(v))
b = v[-1]
c = b[-1]
print(c)   # used to get a particular value in another list


# how to use: insert, append, remove, count(), pop(), reverse()

lst1 = [1, 2, 3]
del lst1[2]
print(lst1)

marks = int[(input("Math: ")), (input("Sci: ")), (input("Eng: ")), (input("Sst: ")), (input("Comp: "))]
print(type(marks))