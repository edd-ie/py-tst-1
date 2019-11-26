"""
Group  of related statement....
syntax of functions:
1  Keyword def marks the start of function header.
                    def - function_name (parameters):
                      	statement(s)
return - statement to recall a value from the function.

"""
p = 0
while p < 10:
    p = p + 1
    print(p, "Hello world")


# defining & creating function
def x_e():
    # function body
    print("hello")
    print("I'm ok")


# call the function
x_e()

q = list(range(1, 7))
r = list(range(10, 19))
s = list(range(20, 30))


def first_in_list(var):
    print(var[-1])


first_in_list(s)


def my_name(name):
    print(name)


my_name("Eddie")


def add_2(a, b):
    ph = a + b
    print(ph)


add_2(10, 20)


def sub_2(a, b):
    diff = a - b
    print(diff)
    return diff


sub_2(23, 20)

z = sub_2(15, 5)


def largest_num():  # Task 6
    print(" Enter 3 Numbers to find Largest")
    kl = [int(input("Enter Num1: ")), int(input("Enter Num2: ")), int(input("Enter Num3: "))]
    print("Largest number is...", max(kl))


largest_num()
