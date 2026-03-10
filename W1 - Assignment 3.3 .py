"""
                                                    Part B — Python Tuples (10 Beginner Questions)

"""

# 1. Create a tuple t = (10, 20, 30) and print the second element.
t = (10, 20, 30)
print(t[1])
print('\n')

# 2. Find the length of tuple ('a', 'b', 'c').
t1 = ('a', 'b', 'c')
print(len(t1))
print('\n')

# 3. Unpack the tuple (4, 5) into variables x and y.
t2 = (4,5)
x,y  = 4,5
print(x)
print(y)
print('\n')

# 4. Check if 'b' is in the tuple ('a', 'b', 'c').
t3 = ('a', 'b', 'c')
print(t3.index('b'))
print('\n')

# 5. Create an empty tuple and print its type.
t = ()
print(type(t))
print('\n')

# 6. Concatenate (1, 2) and (3, 4) into a new tuple.
t4 = (1, 2)
t5 = (3, 4)
con = t4, t5
print(con)
print('\n')

# 7. Repeat (7,) three times.
t6 = (7,)
print(t6*3)
print('\n')

# 8. Find the index of 2 in (1, 2, 3, 2).
t7 = (1, 2, 3, 2)
print(t7.index(2))
print('\n')

# 9. Count how many times 2 appears in (1, 2, 3, 2).
t8 = (1, 2, 3, 2)
print(t8.count(2))
print('\n')

# 10. Create a single‑ element tuple containing the value 5.
t9  = (5,)
print(t9)
