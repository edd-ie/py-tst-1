# unordered collection of items
# stored in unique key_value pair format
# uses {}

d = {
    1: 'orange',  # 1=key orange=value
    2: 'peach',
    3: 'apple'
}
print(d)

detour = {
    "name": "Luis",
    "job": "hobo",
    "age": 24,
    "DOB": {"month": "Nov", "day": 8, "year": 1995}
}
print(detour)
print(detour["job"])  # print a particular value in a dictionary
print(detour["age"])
print(detour["DOB"]["day"])  # used to get a particular value in another value

t = {"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}
u = t.values()
r = list(u)
print(r[0])
