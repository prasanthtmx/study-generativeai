"""1. Create a function area_of_circle(radius) that returns the area using π ≈ 3.14 and includes a docstring.
"""
def area_of_circle(radius):
    return 3.14 * radius * radius
print(area_of_circle(10))
"""    
2. Use an f-string to print:
Name: Alice, Age: 25, Score: 89.5%
"""
name = "Alice"
age = 25
score = 89.5
print(f"Name: {name}, Age: {age}, Score: {score}%")
"""
3. USing an fstring, write a program that takes two numbers from the user and prints:
Sum of <a> and <b> is <sum>
"""
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
sum = a + b
print(f"Sum of {a} and {b} is {sum}")
"""
4. Write a function is_even(num) that returns True if number is even. Add a docstring explaining the logic.
"""
def is_even(num):
    return num % 2 == 0
"""
5. Challenge: Take name and marks as input and print a report card like(use fstring):
Student Report:
---------------
Name: Rahul
Marks: 86.45%
Grade: B+
"""
name = input("Enter your name: ")
marks = float(input("Enter your marks: "))
print("Student Report:
"---------------
Name: {name}
Marks: {marks}%
Grade: B+")
print("---------------")
print(f"Name: {name}")
print(f"Marks: {marks}%")
print(f"Grade: B+")