"""
                                                    Part A — Python Lists (10 Beginner Questions)

"""

# 1. Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.
print('\n')

nums = [3, 1, 4, 1, 5]
print('First Element:',nums[:1:])
print('2nd Element:',nums[:-2:-1])
print('\n')

# 2. Find the length of the list colors = ['red', 'blue', 'green'].
colors = ['red', 'blue', 'green']
print(len(colors))
print('\n')

# 3. Append 'yellow' to the list colors = ['red', 'blue'].
colors.append('yellow')
print(colors)
print('\n')

# 4. Insert 'orange' at index 1 in fruits = ['apple', 'banana'].
fruits = ['apple', 'banana']
fruits[1] = 'orange'
print(fruits)

# 5. Remove 'banana' from fruits = ['apple', 'banana', 'grapes']
fruits = ['apple', 'banana', 'grapes']
fruits.remove('banana')
print(fruits)

# 6. Pop the last element from items = [10, 20, 30] and print the popped value.
items = [10, 20, 30]
items.pop(-1)
print(items)

# 7. Check if 3 is in the list nums = [1, 2, 3, 4].
nums = [1, 2, 3, 9]
print(nums.count(3))

# 8. Print the slice [2, 3] from the list [0, 1, 2, 3, 4].
num = [0, 1, 2, 3, 4]
print(num[2:4])

# 9. Replace the element at index 1 in a = [5, 10, 15] with 12.
a = [5, 10, 15]
a.insert(0, 12)
print(a)

# 10. Count how many times 2 appears in [1, 2, 2, 3, 2].
a = [1, 2, 2, 3, 2]
print(a.count(2))

