"""
                       Part D — Python Dictionaries (10 Intermediate-Level Questions)

"""

# 1. Count word frequencies in a sentence and store the results in a dictionary.
import collections
# txt1 = "the cat and the dog chased the cat"
txt = "Count word frequencies in a sentence and store the results in a dictionary."
frequency = collections.Counter(txt.split())
print("Q1:", frequency)

print('\n')
#2. Invert a dictionary where all values are unique.
dict3 = {'a': 1, 'b': 2, 'c': 3}
f = {v:k for k,v in dict3.items() }
print("Q2:", f)
print('\n')

# 3. Merge two dictionaries where second dictionary overrides first.
dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

dict2 = {
    "product": "Laptop",
    "price": 1200,
    "brand": "Dell"
}

final = (dict2 , dict1)
print("Q3:", final)

print('\n')
# 4. Group words by their first letter into a dictionary of lists.
txt1 = "the cat and the dog chased the cat"
mylist = txt1.split()
list_of_letters = [words[0] for words in mylist]
my_dict = {}
my_dict['letter'] = list_of_letters
print("Q4:", my_dict)
print('\n')

# 5. Filter a dictionary to keep only entries with values greater than 50.
scores = {
    "Alice": 45,
    "Bob": 72,
    "Charlie": 38,
    "David": 91,
    "Emma": 55,
    "Frank": 49
}
d = {k:v for k,v in scores.items() if v > 50 }
print("Q5:", d)
print('\n')

# 6. Given a nested dictionary, safely access a deeply nested key.
data = {
    "user": {
        "profile": {
            "name": "Alice",
            "age": 25,
            "address": {
                "city": "London",
                "zip": "E1 6AN"
            }
        }
    }
}
print("Q6:", data['user']['profile']['address']['city'])
print('\n')

# 7. Write a dictionary comprehension that maps numbers 1–10 to their cubes.
dic = {x: x**3 for x in range(1,11)}
print(dic)
print('\n')

# 8. Find the key with the highest value in a dictionary.
scores1 = {
    "Alice": 45,
    "Bob": 72,
    "Charlie": 38,
    "David": 91,
    "Emma": 55,
    "Frank": 49
}

max_value = max(scores1.values())
print(max_value)
print('\n')

# 9. Combine two lists into a dictionary (keys from first list, values from second).
l1= ['a','b','c']
l2 = [10,20,30]
d5 = dict(zip(l1,l2))
print(d5)

# 10. Remove all keys from a dictionary whose values are None.
s = {
    "Alice": 45,
    "Bob": None,
    "Charlie": None,
    "David": None,
    "Emma": None,
    "Frank": 49
}

update = {k:v for k,v in s.items() if v is not None}
print(update)

