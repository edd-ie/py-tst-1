# used on changeable data
# uses []

x = ["Eren Jaeger", 19, "Attack Titan", "3rd wall district", True]  # to create list {var = [0,1,2...], 0-
print(x)
j = x[-1]
print(j)


r = ["Peter piper", "pick a", "bunch of", "pickled peppers", False]  # to create list {var = [0,1,2...]
print(r)
print(type(r))

v = [x, r]
print(v)
print(type(v))
b = v[-1]
c = b[-1]
print(c)
print(v[2][-1])    # used to get a particular value in another list

# how to use: insert, append, remove, count(), pop(), reverse()

lst1 = [1, 2, 3]
del lst1[2]
print(lst1)