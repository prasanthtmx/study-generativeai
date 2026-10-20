#Student report card generator 

def calculate_toal(marks:list):
    total = 0
    for mark in marks:
        total = total + mark
    return total

def calculate_grade(percentage):
     if percentage>=90:
        return "A"
     elif percentage>=75:
        return "B"
     elif percentage>=60:
        return "C"
     elif percentage>=40:
        return "D"
     else:
        return "F"


print("====Report Card====")

student_name=input("Enter your name: ")
marks=[]

for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total=calculate_toal(marks)
percentage=(total/300)*100
grade=calculate_grade(percentage)

print(f"Name: {student_name}")
print(f"Total: {total}")
print(f"Percentage: {percentage}")
print(f"Grade: {grade}")