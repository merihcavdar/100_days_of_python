student_heights = input("type a list of heights: ").split(",")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height/number_of_students)
print(average_height)

total_height2 = 0
for height in student_heights:
    total_height2+=height
print(total_height2)

number_of_students2 = 0
for student in student_heights:
    number_of_students2 += 1

print(number_of_students2)
average_height2 = round(total_height2/number_of_students2)
print(average_height2)