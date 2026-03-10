"""
                                                Part C — Python Sets (10 Beginner Questions)

"""
print('\n')
# 1. Create a set from [1, 2, 2, 3] and print it.
li = [1, 2, 2, 3]
myset = set(li)
print(myset)
print('\n')

# 2. Add element 4 to the set {1, 2, 3}.
s1 = {1, 2, 3}
s1.add(4)
print(s1)
print('\n')

# 3. Remove element 2 from the set {1, 2, 3}.
s1.remove(2)
print(s1)
print('\n')

# 4. Check if 5 is in the set {1, 3, 5}.
s2 = {1, 3, 5}
s3 = s2.__contains__(5)
print("Contains:", s3)
print('\n')

# 5. Find the length of set {10, 20, 30}.
s4 = {10, 20, 30}
print(len(s4))
print('\n')

# 6. Clear all elements from the set {1, 2, 3}.
clear_set = s4.clear() 
print(clear_set)
print('\n')

# 7. Create a set {'a', 'b'} and add 'c' only if it’s missing.

s5 = {'a', 'b'}
s5.add('c')
print('added', s5)
print('\n')

# 8. Convert list ['a', 'a', 'b'] into a set to remove duplicates.
l1 = ['a', 'a', 'b']
myset1 = set(l1)
print(myset1)
print('\n')

# 9. Create two sets and print their union.
s2 = {1, 3, 5}
s4 = {10, 20, 30}
print(s2.union(s4))
print('\n')

# 10. Create two sets and print their intersection.
print(s2.intersection(s4))
print('\n')