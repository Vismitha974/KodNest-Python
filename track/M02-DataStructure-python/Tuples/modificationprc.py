marks = [70, 80, 60]
stu_marks = marks
stu_marks[0] = 100
print(marks)#[100, 80, 60]
print(stu_marks)#[100, 80, 60]


first = [1, 2, 3]
second = first
print(first is second)#True
print(first == second)#True

first = [1, 2, 3]
second =[1, 2, 3]
print(first is second)#False
print(first == second)#True

#Modification/Mutation:
num = [ 10, 20]
values = num
values.append(30)
print(num)#10, 20, 30
print(values)#10, 20, 30

#Reassignment:
num = [ 10, 20]
values = num
values = [100, 200]
print(num)#10, 20
print(values)#100, 200



# ---------DEEP Copy and NORMAL Copy--------------

# Normal Assignment (not a copy)
original = [[10, 20],[30, 40]]
copy = original
copy[0][0] = 100
print(original)#[[100, 20], [30, 40]]
print(copy)#[[100, 20], [30, 40]]


# Shallow Copy  (.copy) ----new outer list and shared inner list
original = [[10, 20],[30, 40]]
copy = original.copy()
copy[0][0] = 100
print(original)#[[100, 20], [30, 40]]
print(copy)#[[100, 20], [30, 40]]

# Deep Copy (deepcopy(...)) -------new outer and new inner list
import copy
original = [[10, 20],[30, 40]]
cpy_list = copy.deepcopy(original)
cpy_list[0][0] = 100
print(original)#[[10, 20], [30, 40]]
print(cpy_list)#[[100, 20], [30, 40]]