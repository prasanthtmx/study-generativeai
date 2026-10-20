"""
1. Write a program to check if a number is even or odd using if-else.
"""
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
2. Loop through numbers 1 to 10 and print only even numbers using continue.
"""
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

"""
3. Ask the user to guess a number between 1–5. Keep asking until the guess is correct (use while and break).
"""
guess = int(input("Enter a number between 1 and 5: "))
while guess != 3:
    print("Wrong guess")
    guess = int(input("Enter a number between 1 and 5: "))
print("Correct guess")

"""
4. Use a for loop to calculate the sum of all numbers between 1 and 100.
"""
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

"""
5. Write a program to count how many vowels are in a given string using a for loop.
"""
vowels = "aeiou"
string = input("Enter a string: ")
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print(count)

"""
Username: "admin"
Password: "1234"
Allow user 3 attempts. If correct, print "Login successful", else "Account locked".
"""
username = "admin"
password = "1234"
attempts = 0
while attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "1234":
        print("Login successful")
        break
    else:
        print("Invalid username or password")