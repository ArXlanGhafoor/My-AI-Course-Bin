# Loop Manipulation
# 1. Print first 10 natural numbers using while
x = 1
while x<=10:
    print(x, end=" ")
    x += 1

# 2. Take Input from user , and print even number till that input number
user = input("Enter Any Number:") # user = 15
x = 1
while x <= user:
    if x % 2 == 0:
        print(x, end=" ")
    x += 1

# 3. Take Input from user , and print odd number till that input number
user = input("Enter Any Number:") # user = 15
x = 1
while x <= user:
    if x % 3 == 0:
        print(x, end=" ")
    x += 1

# 4. Take Input from user , and print prime number till that input number (For Loop)

user = input("Enter Number") # user = 51
prime = []
for n in range(2, user):
    is_prime = True

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        prime.append(n)

print(prime)

# 4. Take Input from user , and print prime number till that input number (While Loop)
user = input("Enter Number") # user = 51
prime = []
n = 2
while n < user:
    is_prime = True
    

    i = 2
    while i < int(n**0.5)+1:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        prime.append(n)
    n += 1

print(prime)

# 5 Print multiplication table of a given number
x = 1
while x <= 10:
    print(x*7, end=' ')
    x += 1