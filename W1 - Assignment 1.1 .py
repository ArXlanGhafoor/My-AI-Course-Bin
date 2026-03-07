# 1. Write a program to print "Hello, World!" and your name on two separate lines.
print("Hello, World!")
print("Arsalan Ghafoor")

# 2. Ask the user for their favorite color using input() and print "Your favorite color is [color]".
a = input("What is your Favourite color?")

# 3. Use a single print() statement to display three different words separated by a hyphen (-).
print("Ali-Ahmad-Aif")

# 4. Prompt the user for their birth year and print their age (assume the current year is 2026).
user = int(input("Enter Your Birth Year...."))
age = 2026-user
print("Your Age is: ", age)

# 5. Print the result of 5 + 5 such that the output is: The sum of 5 and 5 is 10.
print("Sum = ", 5+5)

# 6. Use the end parameter in print() to join two separate print statements with a space.
print('Apple', end=" ")
print('Mango',end='')

# 7. Write a program that takes two strings from the user and prints them joined together.
str1 = input("Enter Your Name:")
str2 = input("Enter Your Age:")
print(str1, end=' ')
print(str2, end=' ')

# 8. Create a greeting that takes a user's name and prints "Welcome, [Name]!" in all uppercase.

user = input("Enter your Name").upper()
print(f'Welcome {user}!')

# 9. Ask for a user's city and country, then print them in the format: "City, Country".
ask_user1 = input("Ente your city name: ")
ask_user2 = input("Ente your city country name: ")
print(ask_user1, end=', ')
print(ask_user2, end=' ')

# 10. Experiment: What happens if you try to add a string and an integer in a print statement?
a = 10
b = int("5")
print(a+b)
