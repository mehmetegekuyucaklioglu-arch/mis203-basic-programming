students = 0
total = 0

while True:
    name = input("Enter student name (or q to quit): ")

    if name == "q":
        break

    score = int(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score >= 90:
        grade = "AA"
    elif score >= 80:
        grade = "AB"
    elif score >= 70:
        grade = "BA"
    elif score >= 60:
        grade = "BB"
    else:
        grade = "FF"

    print(name, ":", score, "->", grade)

    students = students + 1
    total = total + score

if students == 0:
    print("No students entered.")
else:
    average = total / students
    print("Total students:", students)
    print("Average score:", round(average, 2))
