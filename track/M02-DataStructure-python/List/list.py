numbers = [1, 2, 3, 4, 5, 3]
print(numbers, type(numbers))
print(len(numbers))
print(numbers[1:5])
print(numbers[3:])
print(numbers[-4:-1])

print(numbers[3])


#using constructor
stu = [1, 2, 3, 4, 45.6, True, "ABHI"]
print(stu, type(stu))

#adding elements
num=[1, 2, 3,4]
num.append(6)
num.insert(0, 3)
num.extend([10,20,30])

print(num)
#removing elements
num.pop()
print(num)
num.pop(1)
print(num)
num.remove(20)
print(num)
num.clear()
print(num)
del num

##changing elements