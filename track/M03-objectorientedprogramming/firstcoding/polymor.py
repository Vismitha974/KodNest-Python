#----- Method overloading
# class calculator:
#     def add(self, a, b):
#         print(a+b)
#     def add(self, a, b, c):
#         print(a+b+c)

# obj = calculator()
# # obj.add(10,20) # error
# obj.add(10,20,30) #60

# # 1) Default argument
# class calculator:
#     def add(self, a, b, c=0):
#         print(a+b+c)

# obj = calculator()
# obj.add(10,20) # 30
# obj.add(10,10,10) # 30
# # obj.add(10) # error

# #2) VarArgs
# class calculator:
#     def add(self, *args):
# #         total = 0
#         for i in args:
#             total += 1
#             print(total)

# obj = calculator()
# obj.add() # 0
# obj.add(1,1) # 2
# obj.add(1, 2, 3, 4) # 10

# # 3) KWArgs
# def stu(**kwargs):
#     print(kwargs)
# stu(name="vis", age=22, cgpa=8.9)


#----Method Overriding
# 

#--- DUCK TYPINg
class cat:
    def sound(self):
        print("cats Meow's")

class cow:
    def sound(self):
        print("cow Mow's")

def make_sound(Animal):
    Animal.sound()

ct = cat()
cw = cow()

make_sound(ct)
make_sound(cw)