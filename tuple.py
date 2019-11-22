# unchangeable data
# same as list but use () instead of [] Note elements in tuples can't be deleted or changed

days_of_the_week = ("m", "t", "w", "th", "fr", "sa", "su")

print(len(days_of_the_week))  # calculate number of indexes used
print(days_of_the_week.count("m"))  # count number of times a va,ue appears
print(days_of_the_week[3])  # prints the 3rd index
print(days_of_the_week[1:6])  # prints from indexes 1-6
print(days_of_the_week[-4])  # prints the 4th last index where -1 is last

like = "k", 10, "y", True  # tuple can be written without ()
print(type(like))


ave = 80
if 90 > ave > 60:
    print("Grade= B")

