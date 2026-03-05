# 31. Compare two numbers entered by the user and print if the first is greater than the second.
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))

print("1st Number is greater than 2nd number: ", number1>number2)
print("1st Number is smaller than 2nd number: ", number1<number2)

# 32. Check if a user-entered number is even (Number % 2 == 0) and print the Boolean result.
num = int(input("Enter Number: "))
print(num%2 == 0)

# 33. Write a program that checks if a number is between 10 and 50 (inclusive) using and.
num = 15
print("Number is between 10-50:", num>= 10 and num<=50)

# 34. Check if a string entered by the user is equal to "Python".
user = input("Enter String: ")
Default_input = "python"
print(user == Default_input)

# 35. Use the or operator to check if a user is either "Admin" or "Superuser".
user1 = "user"
print(user1 == "Admin" or user1 == "Superuser")

user2 = "Admin"
print(user2 == "Admin" or user2 == "Superuser")

user3 = "Superuser"
print(user3 == "Admin" or user3 == "Superuser")

# 36. Demonstrate the not operator by reversing a Boolean variable.
a = "Sky is red"
print(not a)

# 37. Compare two floating-point numbers: 0.1 + 0.2 == 0.3. Explain the result.
float1 = 0.1 + 0.2
float2 = 0.3
print(float1 == float2)

# ***Explaination***
#0.1 + 0.2 != 0.3 because Python store decimal numbers in binary numbers. Which alter the actual repreentation of number like 0.1 + 0.3 
# So in backend, the binary representation of the both is diffirent.

# 38. Take a user's age and check if they are NOT under 18.
user = int(input("Enter your age: "))
print(user >= 18)

# 39. Check if a number is positive and odd using logical operators.
num1 = 3
print("Number is odd: ",num1 % 2 != 0)

num2 = 2
print("Number is odd: ",num2 % 2 != 0)

# 40. Compare the lengths of two strings provided by the user.
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
print("Both Strings have equal length: ", len(str1)==len(str2))
print("Both Strings have unequal length: ", len(str1)!=len(str2))
print("Str1 is greater than str2: ",  len(str1)>len(str2))
print("Str1 is smaller than str2: ", len(str1)<len(str2))



