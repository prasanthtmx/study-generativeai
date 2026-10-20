#Practive with variables and data types

"""
Assignment 1:
Create variables to store your:

Name
Age
Favorite programming language
Whether you’re a student (True/False)

Print each of them with appropriate labels using f-strings.
"""
name = "John"
age = 20
favorite_language = "Python"
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite programming language: {favorite_language}")
print(f"Whether you’re a student: {is_student}")

"""
 Assginment 2:
 Predict the output and data types:

x = 10
y = 3.14
z = x + y
print(z)
print(type(z))
"""

x = 10
y = 3.14
z = x + y
print(z)
print(type(z))

"""
Assignment 3:
Create a variable with a value "123" and check if it’s a number or string. Then convert it to an integer and add 10.
"""
value = "123"
print(type(value))
value = int(value)
print(value)
print(type(value))

"""
Assignment 4:
Try creating invalid variable names like 2name, class, or my-name and note what errors Python gives you.
"""

2name = "John"
class = "John"
my-name = "John"
print(2name)
print(class)
print(my-name)

"""
Assignment 5:
Advanced: Can a variable store multiple data types during execution?
""" 
x = 10
print(type(x))

x = "Now I am a string"
print(type(x))