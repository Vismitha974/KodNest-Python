# Neated list and Dictranary

# nested list --list containing list
# stu_marks = [[78, 85, 91], [80, 88, 90]]
# print(stu_marks)

# Nested dictionary --dictionary containing dictionary
# student = {
#     "Name": "vism", 
#     "marks":{"python":77,"sql":88
#     }
# }
# print(student)



# Dict containing lists
# stu = {
#     "Name": "vism", 
#     "marks": [80, 85, 90]
#     }
# print(stu)

# # list containing Dict
# stu_info= [
#     {"name":"Vism",
#     "branch":"ece"
#     },
#     {"name":"Anu",
#     "branch":"cse"
#     }
# ]
# print(stu_info)

#Manually 
from collections import Counter
languages = ["PYTHON", "SQL", "JAVA","PYTHON", "JAVA","PYTHON", ]
frequency = {}
for l in languages:
    if l in frequency:
       frequency[l]+=1
    else:
        frequency[l]=1
print(frequency)

# Using Counter
from collections import Counter
languages = ["PYTHON", "SQL", "JAVA","PYTHON", "JAVA","PYTHON", ]
frequency = Counter(languages)
print(frequency)
print(frequency["Python"])
print(frequency["Java"])

languages = ["PYTHON", "SQL", "JAVA","PYTHON"]
frequency = Counter(languages)
for l, count in frequency.items():
    print(l, count)

letter_counts = Counter("banana")
print(letter_counts)

# Most Common 
skills = ["python"
, "sql",
"java",
"python",
"java",
"python",
 ]
skills_counts = Counter(skills)
print(skills_counts)
frequent_skills = skills_counts.most_common()
print(frequent_skills)

most_requried = skills_counts.most_common(1)

skill = most_requried[0][0]
count = most_requried[0][1]


print(skill)
print(count)