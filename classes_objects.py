class Person:
    species = "homo sapien^2"  # class attribute - each obj will have the attribute

    def walk(self):  # self refers to object created
        print("{} walks" .format(self.name))

p1 = Person()
p1.name = "Reese"
p1.age = 25
p1.state = "alive"
p1.race = "titan"
p1.citizen = True
print(p1.race)
p1.walk()


class Car:
    def make(self):
        print("{} is an SUV".format(self.name))

    def wheel(self):
        print("{} has quad wheels".format(self.name))

    def yom(self):
        print("{} man btwn 09-19".format(self.name))


p1 = Car()
p1.name = "Toyota L.C"
p1.speed = "200, km"
p1.acc = "0-60 in 15s"

p2 = Car()
p2.name = "Merc G"
p2.speed = "220, km"
p2.acc = "0-60 in 10s"

p3 = Car()
p3.name = "Bmw X6"
p3.speed = "260, km"
p3.acc = "0-60 in 6s"

print(p1.name, p1.speed, p1.acc)
p1.make()
p1.yom()

print(p2.name, p2.speed, p2.acc)
p2.make()
p2.yom()

(print(p3.name, p3.speed, p3.acc))
p3.make()
p3.yom()

