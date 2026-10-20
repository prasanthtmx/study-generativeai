#Arithmetic and logical operators
"""
1. Take two numbers as input and print:
Their sum, difference, product, division, and remainder.
"""

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum = int(number1) + int(number2)
difference = int(number1) - int(number2)
product = int(number1) * int(number2)
division = int(number1) / int(number2)
remainder = int(number1) % int(number2)
print(f"The sum of {number1} and {number2} is {sum}")
print(f"The difference of {number1} and {number2} is {difference}")
print(f"The product of {number1} and {number2} is {product}")
print(f"The division of {number1} and {number2} is {division}")
print(f"The remainder of {number1} and {number2} is {remainder}")

"""
2. Ask the user for their age and check:
Are they 18 or older? Print True or False.
"""

age = input("Enter your age: ")
if int(age) >= 18:
    print("True")
else:
    print("False")

"""
3. Ask the user to enter their math and science marks (out of 100). If both are greater than 40, print “Pass”, else “Fail”.
"""

math = input("Enter your math marks: ")
science = input("Enter your science marks: ")
if int(math) > 40 and int(science) > 40:
    print("Pass")
else:
    print("Fail")
"""
4. Check the result of:

x = 7
print(x > 5 and x < 10)
print(x > 10 or x < 5)
print(not(x > 5))
"""
print(x > 5 and x < 10)
print(x > 10 or x < 5)
print(not(x > 5))

"""

5. Challenge: Ask for two numbers and print True if the first number is divisible by the second and greater than it.
"""
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
if int(number1) % int(number2) == 0 and int(number1) > int(number2):
    print("True")
else:
    print("False")