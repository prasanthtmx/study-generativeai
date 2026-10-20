"""
1. Create a list of 5 cities. Then:
Add a new city at the end
Insert one at the 2nd position
Remove the last city and print it
"""
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
cities.append("San Francisco")
cities.insert(1, "Boston")
print(cities.pop())

"""
2. Create a list of numbers: [3, 1, 4, 1, 5, 9]. Then:
Count how many times 1 appears
Sort the list
Reverse the list
"""
numbers = [3, 1, 4, 1, 5, 9]
print(numbers.count(1))
numbers.sort()
numbers.reverse()
print(numbers)

"""
3. Ask the user to enter 3 favorite foods (one by one), store them in a list, and print the final list.
"""
foods = []
for i in range(3):
    foods.append(input("Enter your favorite food: "))
print(foods)

"""
4. Create a list of 4 student names and:
Print the list in reverse (using slicing)
Check if "John" is in the list
"""
student_names = ["Alice", "Bob", "Charlie", "David"]
print(student_names[::-1])
print("John" in student_names)

""" 
5. Challenge:
Create a list of even numbers from 2 to 20 using list repetition or a loop (if already covered).
Store multiple student records in a nested list (e.g., ["Alice", 90])
"""
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(even_numbers)
student_records = [["Alice", 90], ["Bob", 85], ["Charlie", 95], ["David", 80]]
print(student_records)