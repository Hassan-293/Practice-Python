
python_students = [['Harry', 37.21], ['Berry', 37.21],
                  ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

temp = []

for x in python_students:
    temp.append(x[1])
lowest = min(temp)

temp = [value for value in temp if value > lowest]
temp = min(temp)

students = []

for x in python_students:
    if temp == x[1]:
        students.append(x[0])

print(' '.join(students))


