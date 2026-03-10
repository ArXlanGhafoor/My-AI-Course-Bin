                        # Tuple Manipulation#
# 1. Reverse the tuple
mytuple = (1,2,3,4)
tuple_into_list = list(mytuple)
back_into_tuple = tuple(tuple_into_list[::-1])
print(back_into_tuple)

# 2. Access value 20 from the tuple
num = (10,20,30,40,50)
access_value = num[1]
print(access_value)

# 3. Swap two tuples in Python
a = ('milk',)
b = ('Cold-Drink',)
a,b = b,a

print(type(a))
print(type(b))

print(a)
print(b)
