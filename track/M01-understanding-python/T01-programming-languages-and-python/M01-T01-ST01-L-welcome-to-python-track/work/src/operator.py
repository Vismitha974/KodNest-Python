print("------------------------Arithmetic Operators-------------------------")

x = 15
y = 4
print(x + y) #39
print(x - y) #11
print(x * y) #60
print(x / y) #3.75
print(x % y) #3
print(x ** y) #50625
print(x // y) #floor 3


print("------------------------Assignment Operators-------------------------")
x = 10
print("Starting value: x =", x) #10


x = 10
print("\nAfter =  :", x) #10


x += 5
print("After += 5:", x) # x=x+5=15


x -= 3
print("After -= 3:", x) # x= x-3= 12


x *= 2
print("After *= 2:", x) # x=x*2=24


x /= 4
print("After /= 4:", x) # x=x/4=6


x //= 2
print("After //= 2:", x) # 3.0


x %= 3
print("After %= 3:", x) # 0.0


x = 6
print("\nReset x =", x) # 6


x **= 2
print("After **= 2:", x) #36


x = 6
print("\nReset x =", x) #6


x &= 3                    
print("After &= 3:", x) #x = x & 3= 6 & 3


x |= 2
print("After |= 2:", x) # 2


x ^= 5
print("After ^= 5:", x) # 7


x = 4
print("\nReset x =", x) #4


x <<= 2
print("After <<= 2:", x) # 16


x >>= 1
print("After >>= 1:", x) #2





print("------------Comparsion Operators------------------")
x = 5
y = 3


print(x == y) #f
print(x != y) #t
print(x > y) #t
print(x < y) #f
print(x >= y) #t
print(x <= y) #f


print("------------Python allows you to chain comparison operators------")
x = 5
print(1 < x < 10) #t
print(1 < x and x < 10) #t


print("---------------------Logical Operators-------------------------")
a = True
b = False


print("a and b =", a and b) #f
print("a or b  =", a or b) #t
print("not a   =", not a) #f
print("not b   =", not b) #t


x = 10
y = 5


print("\n(x > 5) and (y < 10)  =", (x > 5) and (y < 10)) #t
print("(x < 5) and (y < 10)   =", (x < 5) and (y < 10)) #f


print("\n(x > 5) or (y > 10)  =", (x > 5) or (y > 10)) #t
print("(x < 5) or (y > 10)    =", (x < 5) or (y > 10)) #f


print("\nnot (x == 10) =", not (x == 10)) #f
print("not (y == 3)   =", not (y == 3)) # t


print("----------------Identity Operators------------------")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #t
print(x is y) #f
print(x == y) #t


x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) #checks for values 
print(x is y) #checks for pointing same object 


print("----------------Membership operators--------------------")
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) #t


fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits) #t


text = "Hello World"
print("H" in text) #t
print("hello" in text) #t
print("z" not in text) #f


print("-------------------Bitwise Operators--------------------")
a = 5
b = 3
print("a & b =", a & b) #
print("a | b =", a | b) #
print("a ^ b =", a ^ b) #
print("~a =", ~a) #
print("a << 1 =", a << 1) #
print("a >> 1 =", a >> 1) #


print("----------Ternery operator---------")
x = 4
result = ("Pass" )if x > 5 else ("Fail")
print(result)

#swap to find  the largest of 3 numbers
#swap to find num is positive or negetive