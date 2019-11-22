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

# generate list of numbers x = [1 ,2, 3, 4, 5]
# sort even & odd then print
# simulate a sim pin input if pin is wrong 3 tries deny access

x = range(0, 11)
for num in x:
    if num % 2 == 0:
        print(num, "Even")
    else:
        print(num, "Odd")


pin = 1234
x = 0
while x < 3:
    secure = int(input("Enter Pin: "))
    if secure == pin:
        print("Device Unlocked!")
        break
    else:
        print("Wrong Pin!")
    x += 1









 