# Dictionary Manipulation
dic = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 60,
    "Eva": 95,
    "Frank": 72
}

# 1. Check if a value exists in a dictionary
need_check = 72
result = {value for value in dic.values() if value == need_check}
print(result)

# 2. Get the key of a minimum value from the following dictionary
test = min(dic, key=dic.get)
print(test, dic[test])

# 3. Delete a list of keys from a dictionary
keys_to_remove = ['Alice', 'Bob', 'Eva']
cleaning = {k:v for k,v in dic.items() if k not in keys_to_remove} # dictionary Comprehension
print(cleaning)