# No arguments + No return value 
def add1():
    a, b= 10, 10
    c = a+b
    print(c)
add1()

#No arguments + Return value
def add2():
    a, b= 10, 20
    c = a + b
    return c
print(add2())

#Arguments + No Return value
def add3(a,b):
    c = a+b
    print(c)
add3(10, 50)

#Arguments + Return value
def add4(a, b):
    c = a + b
    return c
res = add4(100,200)
print(res)