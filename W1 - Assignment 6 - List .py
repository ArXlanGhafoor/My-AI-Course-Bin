# 1. Reverse a list in Python
mylist = [1,2,3]
mylist.reverse()
print(mylist)

# 2. Turn every item of a list into its square
num = [1,2,3]
square = [n**2 for n in num] # list comprehension
print(square)

# 3. Remove empty strings from the list of strings
fruits = ["apple", "", "banana", "", "cherry", ""]
clean = [fruit for fruit in fruits if len(fruit)>0] # list comprehension
print(clean)

# 4. Add new item to list after a specified item
newlist = [1,2,3]
newlist.append(4)
print(newlist)

# 5. Replace list’s item with new value if found
list1 = [10,20,30]
list1[0] = "a"
list1[1] = 'b'
list1[2] = 'c'

print(list1)

