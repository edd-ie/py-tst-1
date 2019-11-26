#                                """ Section A"""


def find_grades():  # Task 1
    student = input("Name: ")
    math = int(input("Math: "))
    if math > 100:
        print(student, " Marks don't compute")
    eng = int(input("eng: "))
    if eng > 100:
        print(student, " Marks don't compute")
    kisw = int(input("kisw: "))
    if kisw > 100:
        print(student, " Marks don't compute")
    sci = int(input("sci: "))
    if sci > 100:
        print(student, " Marks don't compute")
    sst = int(input("sst: "))
    if sst > 100:
        print(student, " Marks don't compute")
    tot = int(math + eng + sci + kisw + sst)
    ave = tot / 5
    if ave < 0:
        print(student, " Marks don't compute")
    if ave > 100:
        print(student, " Marks don't compute")
    if 100 > ave > 79:
        print(student, tot, ave, "Grade= A")
    elif 79 > ave > 59:
        print(student, tot, ave, "Grade= B")
    elif 60 > ave > 48:
        print(student, tot, ave, "Grade= C")
    elif 49 > ave > 39:
        print(student, tot, ave, "Grade= D")
    elif 40 > ave > 0:
        print(student, tot, ave, "Grade= E")


find_grades()


def sum_digit(a, b):  # Task 2
    x = a + b
    return x


p = sum_digit(1, 2)
print(p)


#                                               """ Section B"""

def yes_no(a):  # Task 1
    b = "yes"
    c = "Yes"
    d = "YES"
    if a == b:
        return"Yes"
    elif a == c:
        return "yes"
    elif a == d:
        return "yes"
    else:
        return "No"


yes_no()


def large(f, g, h):  # Task 2
    w = [f, g, h]
    w.sort()  # arranges from smallest to largest
    j = w[2]
    return j


def list_a_z(o, s, d, l, b):  # Task 3
    m = [o, s, d, l, b]
    n = [m[0], m[-1]]
    return n


list_a_z()


def even_odd(t):  # Task 4
    if t % 4 == 0:
        return "You Found a multiple of 4..."
    if t % 2 == 0:
        return "Number is Even."
    else:
        return "Number is Odd"


def half_list(a, b, c, d, e, f, g, h):  # Task 5
    h = (a, b, c, d, e, f, g, h)
    n = len(h) / 2
    v = int(n)
    return h[0:v]


#                          """Section C """
def name_open(name):  # Task 1
    return "Hello {} !".format(name)


p = name_open("gerald")
print(p)


def triangle_area(b, h):  # Task 2
    base = b
    height = h
    a_t = (base / 2) * height
    return a_t


triangle_area()


def max_t_edge(a, b, c):  # Task 3
    e1 = a
    e2 = b
    e3 = (e1 + e2) - 1
    if e3 < 0:
        return "Check answer is Negative"
    else:
        return "3rd edge is", e3


max_t_edge()


def list_1st(a):  # Task 4
    m = a
    return m[0]


list_1st()


def leg_calc(a, b, c):  # Task 5
    a *= 2
    b *= 4
    c *= 4
    d = a + b + c
    return d


def largest_num(u, r, y, z):  # Task 6
    v = [u, r, y, z]
    return max(v)


def m_diff(m, n, o, p, q, c):
    mxl = [m, n, o, p, q, c]
    mxl.sort()
    xlr = mxl[-1] - mxl[0]
    return xlr


def comb_lst(a, b):  # Task 8
    return a + b


def length_calc(wr1, wr2):  # Task 9
    if len(wr1) == len(wr2):
        return True
    else:
        return False
