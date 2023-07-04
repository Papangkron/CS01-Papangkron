scoreA = int(input("กรุณาใส่คะเเนนเก็บของคุณ: "))
scoreB = int(input("กรุณาใส่คะเเนนกลางภาคของคุณ: "))
scoreC = int(input("กรุณาใส่คะเเนนปลายภาคของคุณ: "))
if scoreA > 30:
    print("punna gay")
grade = (scoreA + scoreB + scoreC)
if grade > 100:
    grade = "โกง"
elif grade >= 80:
    grade = 'A'
elif grade >= 75:
    grade = 'B+'
elif grade >= 70:
    grade = 'B'
elif grade >= 65:
    grade = 'C+'
elif grade >= 60:
    grade = 'C'
elif grade >= 55:
    grade = 'D+'
elif grade >= 50:
    grade >= 'D'
else:
    grade = 'F'
print("เกรดของคุณคือ: ", grade)