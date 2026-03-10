                                                            ### List ###

# 1. Create a list comprehension that returns the squares of only the even numbers from 0–20. 
list1 = [num for num in range(21) if num % 2 == 0]
# print(list1)

# 2. Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.
nums = [3, 1, 4, 1, 5, 9]
new_num = sorted(nums) # sorted() can sort a list without modifying
# print(new_num) # Modified
# print(nums) # Not Modified

# 3. Remove duplicates from a list while preserving the original order.
# Method 1 - Simplest and easiest
nums2 = [3, 1, 4, 1, 5, 9]
remove_deplicates = list(set(nums2))
print(remove_deplicates)

# Method 2 - List comprehension with enumerates()
remove_deplicates2 = [x for i, x in enumerate(nums2) if x not in nums2[:i]]
print(remove_deplicates2)

# 4. Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension.
l3 = [[1, 2], [3, 4], [5]]
nested = [num for rows in l3 for num in rows]
print(nested)

# 5. Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore case.
names = ['alice', 'Bob', 'charlie', 'DAVID']
new_names = sorted(names, key=str.lower) # 
print(new_names)

'''                             ***Notes*** 
Here is the python orignal order for sorting ['Bob', 'DAVID', 'alice', 'charlie']
Bcs Python prefer capital letters. But we surpass this order by using "key=str.lower

"'''

# 6. Replace items from index 2–4 in a list with [100, 200] using slice assignment.
l4 = [100,200,30,40,50,600]
l4[2:5] = [300,400,500]
print(l4)

# 7. Write a program to find all indices of a value in a list (e.g., all indices of 7).
l5 = [7,14,21,28,35]
updated = [(i,x) for i, x in enumerate(l5) ]
print(updated)

# 8. Create a new list containing only elements that appear exactly once in the original list.
l6 = [1, 2, 2, 3, 4, 4, 5]
new_l6 = [num for num in l6 if l6.count(num) < 2 ]
print('new_l6', new_l6)

# 9. Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]).
l7 = [1,2,3,4]
# print(l7[-1:]) # [4]
# print(l7[:-1]) # [1, 2, 3]
print(l7[-1:] + l7[:-1]) # using concatinaion Technique.

# 10. Split a list into two lists: one with even numbers, one with odd numbers.
l8 = [1,2,3,4,5,6,7,8,9,10]
l8_even = [num for num in l8 if num %2 == 0]
l8_odd = [num for num in l8 if num %2 != 0]
print(l8_even)
print(l8_odd)