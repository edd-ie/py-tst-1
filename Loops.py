def largest_num(u, r, y, z):  # Task 6
    v = [u, r, y, z]
    return max(v)


print(largest_num(4, 5, 1, 3))
print(largest_num(300, 200, 600, 150))


def m_diff(m, n, o, p, q, c):
    mxl = [m, n, o, p, q, c]
    mxl.sort()
    xlr = mxl[-1] - mxl[0]
    return xlr


print(m_diff(10, 15, 20, 2, 10, 6))
print(m_diff(-3, 4, -9, -1, -2, 15))


def comb_lst(a, b):
    return a + b


print(comb_lst([1, 3, 5], [2, 6, 8]))


def length_calc(wr1, wr2):  # Task 9
    if len(wr1) == len(wr2):
        return True
    else:
        return False


print(length_calc("hello", "marshmallow"))


def convert_list(s):  # converting a dict to list
    b = []
    for items in s.items():
        b.append(list(items))
    return b


print(convert_list({"a": 1, "b": 2}))


def profit(t):
    u = t.values()
    r = list(u)
    diff = r[1] - r[0]
    pro = r[2] * diff
    rou = round(pro)
    return rou


print(profit({"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}))


def profit_sim(a):
    prof = int((a["sell_price"] - a["cost_price"]) * a["inventory"])
    v = round(prof)
    return v


print(profit_sim({"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}))


