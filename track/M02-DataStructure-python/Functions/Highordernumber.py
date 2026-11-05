# numbers = [1, 2, 3, 4, 5, 6]

# # square using normal function

# def square(n):
#     return n*n

# result = []
# for i in numbers:
#     result.append(square(i))
# print(result)

# # even using normal function

# def is_even(n):
#     if n % 2 ==0:
#         return True
#     else:
#         return False

# even = []
# for i in numbers:
#     if is_even(i):
#         even.append(i)
# print(even)

# # sum using normal function

# def add(x,y):
#     return x + y

# sum_of_num = 0
# for i in numbers:
#     sum_of_num = add(sum_of_num,i)
# print(sum_of_num)    

# square using higher order function -- map
numbers = [1, 2, 3, 4, 5]
def square(n):
    return n*n
squ = map(square, numbers)
print(list(squ))

# Even using higher order function -- filter

def is_even(n):
    if n % 2  == 0:
        return True
    else:
        return False
even = filter(is_even, numbers)
print(list(even))

# sum using higher order function -- reduce
from functools import reduce
def add(x,y):
    return x + y
sum = reduce(add, numbers)
print(sum)


# Lambda Function 
numbers1 = [1, 2, 3, 4, 5]

# syntax = > lambda arguments: expression

sq = map(lambda x : x * x, numbers1)
print(list(sq))
even = filter(lambda x : x % 2 == 0, numbers1)
print(list(even))
sum = reduce(lambda x,y: x + y, numbers1)
print(sum)