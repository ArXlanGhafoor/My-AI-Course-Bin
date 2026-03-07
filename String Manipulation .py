# 1. Write a program to create a new string made of an input string’s first,middle, and last character.
user = input("Write a setence: ") # 
user = "Write a program to create a new string made of an input strings first,middle, and last character."
print("First Character:", user[:1:])
print("Last Character:", user[-1::])
print(len(user)//2) # to check middle index.
print("Last Character:", user[48:50:])

# 2. Write a program to count occurrences of all characters within a string Given.
a = "python"
print("Total Character:", len(a))

# 3. Reverse a given string
print(user[::-1])

# 4. Split a string on hyphens
txt = 'learning-python-is-fun'
print(txt.split('-'))

# 5. Remove special symbols / punctuation from a string
import re
text = "apple,,,banana;;cherry!!!mango2026"
cleaning = re.split(r'[^a-zA-Z]+', text)
print(cleaning)


