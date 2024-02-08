students = {}

while True:
    name = input("Enter student's name or 'X' to stop: ")
    if name.upper() == 'X':
        break

    mark = int(input("Enter student's exam mark (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid mark! Mark should be between 0 and 100.")
        continue

    students[name] = mark

if students:
    best_student = max(students, key=students.get)
    best_mark = students[best_student]
    average_mark = sum(students.values()) / len(students)

    print(f"The best student is {best_student} with a mark of {best_mark}.")
    print(f"The average mark for all students is {average_mark:.2f}.")
else:
    print("No students entered.")
