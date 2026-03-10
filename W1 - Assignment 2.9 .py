"""
                                            Part C — Python Sets (10 Intermediate-Level Questions)
"""


# 1. Given two sets, find elements that are in the first set but not the second.
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a-b)

# 2. Find common items between three sets using intersection.
a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = {2,4,5,7,9}

int1 = a.intersection(b)
int2 = int1.intersection(c)
print(int2)

# 3. Given a sentence, return all unique words in lowercase.
sentence = "The cat chased the mouse, and the cat climbed the tree while the mouse ran away."
unique_words = set(sentence.lower().split())
print(unique_words)

# 4. Convert a list with duplicates into a set, then back to a sorted list.
list1 = [1,2,5,5,7,7,4,4]

list_into_set = set(list1)
set_into_list = list(list_into_set)
print(set_into_list)

# 2nd way.
print('sorted:', sorted(set(list1))) 

# 5. Check if one set is a strict subset of another.
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))

# 6. Use a set comprehension to collect all squares of numbers from 1–15 that are divisible by 3.
new_set = {num for num in range(1,16) if num % 3 ==0}
print(new_set)

# 7. Count how many duplicate values exist in a list using sets.
mylist = [1,1,2,2,3,4,5]
print(len(mylist)-len(set(mylist)))

print('\n')
# 8. Write a program to remove all vowels from a string using a set.
mystr = "Count how many duplicate values exist" 
splitted = mystr.split()       
vowel = {'a','e','i','o','u'} 
mylist = ''.join(characters for characters in mystr if characters.lower() not in vowel)
print(mylist)
print('\n')

# 9. Find the symmetric difference between two sets.
A = {1, 2}
B = {1, 2, 3, 4}
print(A.symmetric_difference(B))

# 10. Check if two strings are anagrams using set comparison (unique characters only).
str1 = "listen"
str2 = "silent"
print(True if sorted(set(str1)) == sorted(set(str2)) else False) # to maintain duplication use sorted()