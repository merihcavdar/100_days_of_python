student_scores = input("type a list of student scores separated by comma: ").split(",")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
print(max(student_scores))

maksimum = 0
for score in student_scores:
    if score > maksimum:
        maksimum = score

print(f"the highest score is {maksimum}")
