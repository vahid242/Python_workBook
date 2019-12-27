x=3
name = "ali"
city = 'syz'
grades=[3,4,5]
student_grade={"tom": 5, "jerry":6, "locus":2}
print(x,  name, city)
print(grades)
print(type(x), type(name), type(city))
sumGrade = sum(grades)
print(sumGrade)
print(max(grades))
print(grades.count(4))
print(student_grade.values())
print(sum(student_grade.values()))
print(student_grade.keys())
print(student_grade.items())
print(len(student_grade))

