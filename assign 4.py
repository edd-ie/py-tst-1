x = 0
while x < 100:
    x = x + 1
    print("Eddie")   # Task 1

y = 0
while y < 100:
    y = y + 1
    print(y, "Eddie")  # Task 2

z = 8
while z < 89:
    z = z + 1
    print(z)   # Task 3

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)