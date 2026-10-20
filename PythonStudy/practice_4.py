"""1. Write a program that:
Asks the user to enter two numbers
Adds and multiplies them
Prints both results
"""
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum = int(number1) + int(number2)
product = int(number1) * int(number2)
print(f"The sum of {number1} and {number2} is {sum}")
print(f"The product of {number1} and {number2} is {product}")

"""
2. Introduce an error:
Try adding a string and an integer
Fix it using typecasting

"""
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum = int(number1) + int(number2)
product = int(number1) * int(number2)
print(f"The sum of {number1} and {number2} is {sum}")
print(f"The product of {number1} and {number2} is {product}")
print(f"The sum of {number1} and {number2} is {sum}")
print(f"The product of {number1} and {number2} is {product}")
print(f"The sum of {number1} and {number2} is {sum}")
print(f"The product of {number1} and {number2} is {product}")
print(f"The sum of {number1} and {number2} is {sum}")

"""
Create a program that:
Asks for name and age
Prints: Hi <name>, you will be 100 years old in the year <calculated_year>

"""
name = input("Enter your name: ")
age = input("Enter your age: ")
years_left = 100 - int(age)
print(f"Hi {name}, you will be 100 years old in the year {years_left}")



"""
4. Write a buggy program that crashes, then fix it:

--python code:--
# Bug: input not converted to int
age = input("Enter your age: ")
years_left = 100 - age
print("Years left to turn 100:", years_left)
--python code:--
"""
age = input("Enter your age: ")
years_left = 100 - int(age)
print("Years left to turn 100:", years_left)
