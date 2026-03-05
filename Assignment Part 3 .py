# 21. Write a program to calculate the area of a rectangle (Length × Width).
length = 5
width = 10
area_of_rectangle = length * width
print(area_of_rectangle)

# 22. Take two numbers and print the result of the first raised to the power of the second (a^b).
a = 2
b= 3
print(a**b)

# 23. Demonstrate the difference between / (division) and // (floor division) with the numbers 10 and 3.
a = 10
b = 3
print("Division", a/b)
print("Floor Division", a//b) # also know as round off division.

# 24. Use the modulus operator % to find the remainder when 25 is divided by 4.
print(25%4) # modulus operator % use to find the remainder.

# 25. Calculate the average of five numbers entered by the user.

                                    #Method 1:
# int(input()) can't wor bcs it will convert into a single number.
# That's why here we use list comprehension.
# list comprehension: [expression for variable in iterable]
# numbers = [int(n) for n in numbers.split(",")]

numbers = (input("Enter the five numbers seperated by comma "))
numbers = [int(n) for n in numbers.split(",")]
print("Average of the Numbers is: ", sum(numbers)/len(numbers))

                                    # Method 2:
number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number2: "))
number3 = int(input("Enter the number3: "))
number4 = int(input("Enter the number4: "))
number5 = int(input("Enter the number5: "))

numbers = [number1,number2,number3,number4,number5]  #store numbers in a list
print("Average of the Numbers is: ", sum(numbers)/len(numbers))

# 26. Create a program that converts minutes into hours and remaining minutes.
mints = 100
hours = 100//60
Remaining_mints = 100%60

print("Hours = ", hours)
print("Remaining Mint = ",Remaining_mints)

# 27. Calculate the area of a circle where Area = \pi r^2 (Use 3.14 for \pi).
r = 5
area_of_circle = 3.14 *r**2
print("Area of the Circle = ", area_of_circle)

# 28. Find the cube of a number entered by the user.
a = 2
print("Cube of 2 = ", a**3)

# 29. Perform the calculation 10 + 5 * 2. Does Python follow PEMDAS? Prove it with code.
result1 = 10 + 5 * 2
result2 = (10 + 5) * 2 
print("Experience PAMDAS without paranthesis: ", result1)
print("Experience PAMDAS with paranthesis: ", result2)

# 30. Write a program to calculate simple interest: (P \times R \times T) / 100.
P = 1000
R = 10 
T = 2

interest = P*R*T/100
print(interest)