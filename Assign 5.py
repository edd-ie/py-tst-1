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

def yes_no():  # Task 1
    print("Do you agree with the terms:")
    a = str(input(" Enter Answer: "))
    b = "yes"
    c = "Yes"
    d = "YES"
    if a == b:
        print("Yes")
    elif a == c:
        print("yes")
    elif a == d:
        print("yes")
    else:
        print("No")


yes_no()


def large():  # Task 2
    print(" Enter 3 Numbers to find Largest")
    w = [int(input("Enter Num1: ")), int(input("Enter Num2: ")), int(input("Enter Num3: "))]
    w.sort()  # arranges from smallest to largest
    print("Largest number is...", w[2])


large()


def list_a_z():  # Task 3
    print("Enter a list of 5 numbers...")
    m = [int(input("Enter Num1: ")), int(input("Enter Num2: ")), int(input("Enter Num3: ")), int(input("Enter Num4: ")),
         int(input("Enter Num5: "))]
    n = [m[0], m[-1]]
    print("First & Last in the list: ", n)
    print("First & Last in the list: ", [m[0], m[-1]])  # Shorter alternative than creating a new var


list_a_z()


def even_odd():  # Task 4
    print("Identify a Number if even/odd")
    q = int(input("Enter a Number: "))
    if q % 2 == 0:
        print("Number is Even.")
    else:
        print("Number is Odd")
    if q % 4 == 0:
        print("You Found a multiple of 4...", q)


even_odd()


def half_list():  # Task 5
    h = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    n = len(h) / 2
    v = int(n)
    print(h[0:v])


half_list()


#                          """Section C """
def name_open(name):  # Task 1
    return "Hello {} !".format(name)


p = name_open("gerald")
print(p)


def triangle_area():  # Task 2
    base = int(input("Base Length: "))
    height = int(input("height Length: "))
    a_t = (base / 2) * height
    print("Area is ", a_t)


triangle_area()


def max_t_edge():  # Task 3
    e1 = int(input("1st edge: "))
    e2 = int(input("2st edge: "))
    e3 = (e1 + e2) - 1
    if e3 < 0:
        print("Check input value Negative")
    else:
        print("3rd edge is", e3)


max_t_edge()


def list_1st():  # Task 4
    print("Enter a list of 5 numbers...")
    m = [int(input("Enter Num1: ")), int(input("Enter Num2: ")), int(input("Enter Num3: ")), int(input("Enter Num4: ")),
         int(input("Enter Num5: "))]
    print("First in the list: ", m[0])


list_1st()


def leg_calc():  # Task 5
    print("Enter number of animals to get leg count...")
    ch = int(input("Num of chickens: "))
    cw = int(input("Num of cows: "))
    pg = int(input("Num of pigs: "))
    cn = (ch * 2) + (cw * 4) + (pg * 4)
    print("Leg count is: ", cn)


leg_calc()


def large2():  # Task 6
    print(" Enter 3 Numbers to find Largest")
    kl = [int(input("Enter Num1: ")), int(input("Enter Num2: ")), int(input("Enter Num3: "))]
    print("Largest number is...", max(kl))


large2()


def m_diff():  # Task 7
    print("Enter a list of 5 numbers...")
    mxl = [int(input("Enter Num1: ")), int(input("Enter Num2: ")), int(input("Enter Num3: ")),
           int(input("Enter Num4: ")),
           int(input("Enter Num5: "))]
    mxl.sort()
    print("Diff btwn Largest & smallest : ", mxl[-1] - mxl[0])


m_diff()


def comb_lst():  # Task 8
    print(" Enter 1st list")
    ls1 = [input("Enter object1: "), input("Enter object2: "), input("Enter object3: ")]
    print(" Enter 2nd list")
    ls2 = [input("Enter object1: "), input("Enter object2: "), input("Enter object3: ")]
    ls3 = ls1 + ls2
    print(ls3)


comb_lst()


def length_calc():  # Task 9
    print("Calculate if words have equal lengths...")
    wr1 = str(input("1st word:"))
    wr2 = str(input("2nd word:"))
    if len(wr1) == len(wr2):
        print(True, "words equal")
    else:
        print(False, "words unequal")


length_calc()



