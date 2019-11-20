"""
special symbols for arithmetic & logic computation
Arithmetic ops - perform simple math + - * /
               - % = remainder
               - // = no decimal place division
               - ** = exponent 3^2

 Comparison Operators - to compare values
                                        } -  Conditional Operators check the following:
                                        } -  < less than
                                        } -  > greater than
                                        } -  == (Check equality)
                                        } -  != (Check Inequality)
                                        } -  <> (Check equality)

"""

w = 355
x = 600
y = 455
z = 934
m = 4
n = 2

print(w * x + y - z)
print(m ** n)
print(m % n)

# r = input("Enter Number:")  # use input(..) for acquiring user input
# z = input("Enter Number:")
# v = int(r) ** int(z)  # the ops to work convert the var to an int()
# print(v)

a = 5
b = 7
c: int = 10

print("a<b is", a < b)
print("a==b", a == b)

if a == b:
    print("savvy")
else:
    j = a + 2
    print(j)

k = 2 < 5
o = 5 < 2
print("k and o is", k and o)  # and - All conditions have to be true, 5 is not < 2 = false
print("k or o is", k or o)  # or - At least one condition is true,  2 is < 5 = true
print("not o is", not o)  # displays the opposite, 5 is not < 2 = true

c = 10
c += 10
print(c)

i = 4
i *= 3
print(i)

# Research on membership & identity operators

flop = input("Enter Cash Amount:")
if int(flop) < 200:
    print("Insufficient Amount add", 200 - int(flop))
else:
    print("Welcome What Flavor coffee", "Balance", int(flop) - 200)

print("I can Multiply Anything try me")
pst = int(input("1st Number:"))
mmh = int(input("2nd Number:"))
print("Answer:", pst * mmh, "told you I'm a wizard")