                                                            ### Tuples ###

# 1. Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.


l1 = [1, 2, 3, 4]
mytuple = tuple(l1)
a,b,c,d = mytuple # unpacking
print(a,b,c,d)

# 2. Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.
t = (('a', 1), ('b', 2), ('c', 3))
mylist = [num[1] for num in t ]
print(mylist)

# 3. Write a function that returns multiple values (sum, min, max) using a tuple. 
l2 = [3, 7, 2, 9, 5]
def calculate(num):           # fn with parameter num
        # list into tuple with sum, min and max.
        l2_sum = sum(num)
        l2_min = min(num)
        l2_max = max(num)
        return(l2_sum, l2_min, l2_min) #return values

a,b,c = calculate(l2) # unpacking and recall the function with argument l2
print(a, b, c)        # as we return the fn so have to use print

# 4. Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list.
concate = (1, 2, 3) , (4, 5)
print(concate)

# 5. Given a tuple of numbers, find the element with the highest frequency.
t4 =(1,2,3,6,6,6,5,7,8,9,9,9,9,9,9,9)

# to count the frequency with max() and lambda (shortest way)
maximum_count = (max(set(t4), key=lambda x: t4.count(x)))
print('lmbda...', maximum_count)

# to count the frequency of all elements
import collections
new = collections.Counter(t4)
print('collection...',new)


# to count the frequency of specif elements
t4 =(1,2,3,6,6,6,5,7,8,9,9,9,9,9,9,9)
unique_set = set(t4)   # to avoid repitition of same number, we typecast tuple-set.
highest_element = None # here we are assuming, we dont have highest element.
max_count = 0          # Also we assume, our max_count is 0

for x in unique_set:   # insert loop on repitition free set.
        if t4.count(x) > max_count:         
                max_count = t4.count(x)
                highest_element = x
print('loop...',highest_element)

# 6. Check if two tuples contain the same elements regardless of order.
t1 = (1, 2, 3, 4)
t2 = (4, 3, 2, 1)

tuple1 = sorted(t1)
tuple2 = sorted(t2)

True if tuple1 == tuple2 else False

# 7. Extract the last three items from a tuple using slicing.

t3 = (3, 7, 2, 9, 5, 8)
print(t3[-3::])


# 8. Concatenate a tuple with itself three times (repeat operation).
t3 = (1,2,3)
print(t3*3)

# 9. Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).
t4 = ((1,2),(3,4))
tt = [num for rows in t4 for num in rows]
print(tuple(tt))

# 10. Store coordinates in tuples and calculate the Manhattan distance.
p1 = (1,2)
p2 = (4,5)
Manhattan_Distance = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) #abs(x1-x2) + abs(y1-y2)
print("Manhattan_Distance:", Manhattan_Distance)

