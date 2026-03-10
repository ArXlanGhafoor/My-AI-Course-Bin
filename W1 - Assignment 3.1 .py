"""
                                                Part D — Python Dictionaries (10 Beginner Questions)

"""
# 1. Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
dic1 = {'name': 'Ali', 'age': 25}
print(dic1['name'])

# 2. Add key 'city': 'Lahore' to a dictionary.
dic1.update({'city':'Lahore'})
print(dic1)

# 3. Change 'age' in {'name': 'Ali', 'age': 25} to 30.
dic1['age'] = 30
print(dic1)

# 4. Delete key 'age' from a dictionary.
dic1.pop('age')
print(dic1)

# 5. Check if key 'salary' exists in a dictionary.
print(dic1.get('salary'))

# 6. Print all keys from.
dict2= {'a': 1, 'b': 2}
print(dict2.keys())

# 7. Print all values from a dictionary.
print(dict2.values())

# 8. Iterate and print key‑ value pairs from {'x': 10, 'y': 20}.
dct3 = {'x': 10, 'y': 20}
iterate = {k:v for k,v in dct3.items()}
print(iterate)

# 9. Use get() to safely read key 'score' from an empty dictionary.
empty_dict = {}
print(empty_dict.get('score'))

# 10. Create a dictionary from two lists: keys = ['a','b'], values = [1,2].
keys = ['a','b']
values = [1,2]
dct4 = dict(zip(keys, values))
print(dct4)