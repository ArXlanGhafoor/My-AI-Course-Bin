# 11. Create an integer variable age and a float variable height. Print their types.
age = 27
height = 5.2
print(type(age))
print(type(height))

# 12. Store the value 3 + 4j in a variable. Print the variable and its type.
var = 3 + 4j
print(var)
print(type(var))

# 13. Create a boolean variable is_python_fun and set it to True.
is_python_fun = True
print(is_python_fun)
print(type(is_python_fun))

# 14. Method 1: Assign three different values to three variables in a single line.
a,b,c = 1,2,3
print(a,b,c)

# 15. Method 2: Assign the same value to three different variables in a single line.
a = b = c = 10
print(a,b,c)

# 16. Take a numeric input from a user and convert it to a float.
user = int(input('Enter your age: '))
user_typecasting = float(user)
print(type(user_typecasting))

# 17. Take a string input "100" and convert it to an int.
mystr = int("100")
print(type(mystr))

# 18. Create a variable with a complex number and print only its real part.
a = 1 + 2j
print("Real Part of Imaginagry Number = ", a.real)
print("Imaginary Part of Imaginagry Number = ", a.imag)

# 19. Define a string variable containing a paragraph and print its length.
mystring = """Learning new skills requires patience, consistency, and curiosity. 
When people start studying something unfamiliar, such as programming or mathematics, the beginning can feel confusing and overwhelming. 
However, with regular practice and a willingness to make mistakes, complex ideas slowly become clearer. 
Each small step of progress builds confidence and strengthens understanding. 
Over time, what once seemed difficult becomes natural, and the learner develops the ability to solve problems more efficiently and creatively."""

print(len(mystring))

# 20. Swap the values of two variables a and b without using a third variable.
a = "Juice"
b = "Water"
a,b = b,a
print("a =", a)
print("b =", b)

# 21. Swap the values of two variables a and b with using a third variable.

a = "Milk"
b  = "COld-Drink"

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)