# class parent:
#     p1 = 1200
#     p2 = 1200
# class child(parent):
#     p3 = 2400
# chi = child()
# print(chi.p1)
# print(chi.p2)
# print(chi.p3)


class Employee:
    def __init__(self, name, age, salary, role):
        self.name = name
        self.age = age 
        self.salary = salary
        self.role = role
    #Inherited method
    def display_info(self):
        print(f"name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Role: {self.role}")
    
    #method to be overridden
    def work(self):
        print("Employee is working")

#child class ---Developer
class Developer(Employee):
    # overriding method
    def work(self):
        print("Development work")
    # specialized method
    def project(self, project_name):
        print("Developer is developing project: {project_name}")

#child class ---Tester
class Tester(Employee):
    # overriding method
    def work(self):
        print("Testing work")
    # specialized method
    def project(self, project_name):
        print("Tester is testing project: {project_name}")

dev = Developer("Vismitha", 22, 500000, "Developer")
test = Tester("Shamanth", 24, 700000, "Tester")

print("------Developer-------")
dev.display_info() #Inherited
dev.work()         #Overridden
dev.project("Bank App")#Specialized

print("------Tester-------")
test.display_info() #Inherited
test.work()         #Overridden
test.project("E-commerce App")#Specialized
