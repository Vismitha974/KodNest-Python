c = 30
def add():
    a = 10 # local Variable
    b = 30
    print(a + b) 
    print(c) # global Variable
add()
print(c) # global Variable


# print(f"The value of a is {a}") # global variable
# print(a + b)

x = 100 # global variable
def display():
    x = 50 # local variable
    print("Local x:", x) # 50
display()
print("Global x:", x) # 100

x = 10 # global variable
def display():
    print(x) # 10
    #x = 20 # local variable
display()
x = 20
print(x)


### Recursion 

def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
count(5)

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)
print(fact(5))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(5))    