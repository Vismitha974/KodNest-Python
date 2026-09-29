# Inbuilt String Methods – Single Program
s = "  kodNest Technologies 123  "


print("Original String:", s) #  kodNest Technologies 123  


# Case conversion methods
print("upper():", s.upper()) # KODNEST TECNOLOGIES 123
print("lower():", s.lower()) #   
print("capitalize():", s.capitalize()) #  
print("title():", s.title()) #  
print("swapcase():", s.swapcase()) #


# Searching & counting
print("find('Tech'):", s.find("Tech")) # 
print("count('o'):", s.count("o")) #


# Replace
print("replace('123', '2025'):", s.replace("123", "2029"))


# Start & End check
print("startswith('  kod'):", s.startswith("  kod")) #
print("endswith('123  '):", s.endswith("123  ")) #


# Split & Join
words = s.split() #
print("split():", words)
print("join():", "-".join(words)) # 


# Strip spaces
print("strip():", s.strip()) # kodnest technologies 123
print("lstrip():", s.lstrip())# 
print("rstrip():", s.rstrip())#  


# Checking methods
print("isalpha():", s.isalpha())#False
print("isdigit():", s.isdigit())#False
print("isalnum():", s.isalnum())#False


# Length
print("Length of string:", len(s))