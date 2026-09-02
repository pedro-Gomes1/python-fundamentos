students = {}

for i in range(10):

    number = int(input("Enter the student's number: "))
    height = float(input("Enter the student's height in cm: "))

    students[number] = height

print("\nRegistered students:")
print(students)

shortest_height = min(students.values())
tallest_height = max(students.values())

for number, height in students.items():

    if height == tallest_height:
        print(f"Student {number} is the tallest: {height} cm")

    if height == shortest_height:
        print(f"Student {number} is the shortest: {height} cm")
