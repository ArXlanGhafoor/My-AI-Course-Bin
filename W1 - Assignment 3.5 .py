"""
                                                        Beginner Level String Tasks

"""
print('\n')
# 1. Write a program that reads a string and prints its length.
myInput = "hello world"
print(len(myInput))
print('\n')

# 2. upper and lower case
str1 = "Python3"
print(str1.upper())
print(str1.lower())
print('\n')

# 3. Count how many times a given character appears in a string (case-sensitive).
str2 = "banana"
print(str2.count('a'))
print('\n')

# 4. Print the first and last character of a string; handle empty input.
str3 = "drawer"
print(str3[0])
print(str3[-1])
print('\n')

# 5. Acces "science"
str4 = "data science"
print(str4[5:])
print('\n')

# 6. Access "gram"
str5 = 'programming'
print(str5[3:7])
print('\n')

# 7. Reverse
str6 = "Python"
print(str6[::-1])
print('\n')

# 8. Replace
str7 = "I love apples. Apples are great!"
newstr = str7.replace("apples","oranges")
print(newstr)
print('\n')


# 9. Split on spaces and join with "-"
str8 = "split this sentence" 
new1 = str8.split()
new2 = '-'.join(new1)
print(new2)
print('\n')

# 10. Remove front and back spaces.
str9 ="   padded text  "
new = str9.strip()
print(new)
print('\n')