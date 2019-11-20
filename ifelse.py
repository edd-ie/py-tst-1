pasta = input("Enter Cash Amount:")
if int(pasta) < 200:
    print("Insufficient Amount add", 200 - int(pasta))
else:
    print("Welcome What type pasta do you like", "Balance", int(pasta) - 200)

snap = input("Enter Number of Infinity stones acquired :")
if int(snap) < 5:
    print("Insufficient Amount add", 5 - int(snap))
elif int(snap) > 5:
    print("Mortal You Can't fool the Infinity goblet")
elif int(snap) == 5:
    print("Welcome Thanos The Universe is yours!")

num = input("Enter Number to know if pos/neg :")
if int(num) < 0:
    print("Number is Neg", "add", 0 - int(num), "to be positive")
elif int(num) > -1:
    print("Number is Positive")
