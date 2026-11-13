# 1)Single Inheritance
# One child class inherits from one parent.
class Vehicle:
    def start(self):
        print("Vehicle starts")
class car(Vehicle):
    pass

c = car()
c.start()

#Flow vehicle--->car

# 2)Multiple Inheritance
# One child class inherits from multiple parent.
class Engine:
    def engine_type(self):
        print("Petrol engine")
class Wheels:
    def wheel_count(self):
        print("4 wheels")
class Car(Engine, Wheels):
    pass
c = Car()
c.engine_type()
c.wheel_count()

#Flow Engine--->Wheels---->car

# 3)Multilevel Inheritance
# A chain of Inheritance.
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def drive(self):
        print("Car drive")
class SportsCar(Car):
    def speed(self):
        print("Very fast")
s = SportsCar()
s.start()
s.drive()
s.speed()

#Flow: vehicle--->Car---->SportsCar

# 4)Hierarchical Inheritance
# Multiple child classes inherits from one parent.
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass

c = Car()
b = Bike()
c.start()
b.start()

# Flow:   Vehicle
#          /    \
#        Car    bike

# 5)Hybrid Inheritance
# combination of two or more inheritances
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Engine(Vehicle):
    def engine(self):
        print("Engine working")

class Wheels:
    def wheels(self):
        print("wheels rolling")

class Car(Engine, Wheels):
    pass

c = Car()
c.start()
c.engine()
c.wheels()

# Flow: ombination of hierarchy


# Quick Summary Table
# Type         Parent -> Child
# Single       1 Parent -> 1 Child
# Multiple     Many Parents -> 1 Child
# Multilevel   Chain (Grandparent -> Parent -> Child)
# Hierarchical 1 Parent -> Many Children
# Hybrid       Combination of above