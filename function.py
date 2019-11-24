"""
Group  of related statement....
1  Keyword def marks the start of function header.
                    def - function - name (parameters):
                      	statement(s)


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
    return diff


sub_2(23, 20)

z = sub_2(10, 5)
print(z)


