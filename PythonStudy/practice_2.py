#Practice input functions
"""
1. Ask the user for:
Their name
Their birth year

Then print: Hello <name>, you are <age> years old!
"""

name = input("What is your name? ")
birth_year = input("What is your birth year? ")
age = 2026 - int(birth_year)
print(f"Hello {name}, you are {age} years old!")

"""
2. Ask the user for two numbers and print:
Their sum
Their difference
Their product
"""

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum = int(number1) + int(number2)
difference = int(number1) - int(number2)
product = int(number1) * int(number2)
print(f"The sum of {number1} and {number2} is {sum}")
print(f"The difference of {number1} and {number2} is {difference}")
print(f"The product of {number1} and {number2} is {product}")

"""
3. Ask the user to enter a float number and cast it to integer. Print both values.
"""

float_number = input("Enter a float number: ")
int_number = int(float_number)
print(f"The float number is {float_number} and the integer number is {int_number}")

"""
4. Ask the user to enter two words and print them in reverse order, separated by a comma.
Example:

Input 1: Hello
Input 2: World
Output: World, Hello
"""

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(f"{word2}, {word1}")

"""     
5. Challenge: Ask for a number, multiply it by 5, then convert the result to a string and print:
"Your number multiplied by 5 is: <result>"
"""

number = input("Enter a number: ")
result = int(number) * 5
print(f"Your number multiplied by 5 is: {result}")
