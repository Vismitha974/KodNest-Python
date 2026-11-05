# # Square


# square =  [i*i for i in range (1,6)]
# print(square)


# # Even



# Even = [ i for i in range(1, 11) if i % 2 == 0]
# print(Even)

# # Upper

# names = ["vis" , "sam"]
# new_list = [name.upper() for name in names]
# print(new_list)


# # Greater than 10 

# num = [ 11, 2, 12, 4, 17, 8]
# ne_list = [i for i in num if i >= 10]
# print(ne_list)


# Sorted()
from os import name
marks = [20, 13, 40, 5]
new_marks = sorted(marks , reverse = True)
print(new_marks)
print(marks)

# Sort()
age = [2, 18, 100 , 90]
age.sort(reverse=True)
print(age)

names = ["apple" ,  "mango" , "banana"]
names.sort()
print(names)

names = {"apple" ,  "mango" , "banana"}
print(sorted(names))

# cannot be used
names = {"apple" ,  "mango" , "banana"}
names.sort()
print(names) # through error




# Cube of Numbers: 
# Create a list of cubes of numbers from 1 to 10 using list comprehension.
# Positive Numbers: 
# Extract all positive numbers from a given list.
# nums = [-5, 10, -2, 20, 0, 15, -8]
# Words Starting with a Vowel: 
# Extract all words that start with a vowel.
# words = ["Apple", "Banana", "Orange", "Grapes", "Umbrella"]
# Even or Odd: 
# Create a list that labels each number as "Even" or "Odd" for numbers from 1 to 10.
# Extract Vowels:
#  Extract all vowels from a given string using list comprehension.
# text = "programming"
# Word Lengths: 
# Create a list containing the length of each word.
# words = ["Python", "Java", "React", "Django"]
# Remove Duplicates:
#  Remove duplicate elements from a list while preserving the original order.
# nums = [1, 2, 3, 2, 4, 1, 5]
# Flatten a Nested List: Convert a nested list into a single list.
# matrix = [[1, 2], [3, 4], [5, 6]]
# Find Common Elements: Find elements present in both lists using list comprehension.
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# Find Prime Numbers: Generate all prime numbers between 1 and 100 using list comprehension.