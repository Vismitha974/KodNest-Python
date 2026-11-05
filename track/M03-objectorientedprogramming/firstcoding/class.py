class Student:
    #Constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    # name = "Vismitha"
    # age = 22
    # gender = "female"

    def study(self):
        print(f"{self.name} is studying {self.age} years")

    def eat(self):
        print(f"{self.name} is playing {self.age} years")

s1 = Student("vismitha", 22, "female")
s2 = Student("shamanth", 24, "male")
print(f"Name: {s1.name}")
print(f"Name: {s2.name}")
# print(s1.name)
# print(s1.age)
# print(s1.gender)

s1.study()
s1.eat()
s2.study()
s2.eat()