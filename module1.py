grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=list(students)
students=(sorted(students))
def average(grades):
   return sum(grades) / len(grades)
average_grades = [average(grade) for grade in grades]
print(average_grades)
print(students)
grades_dict = dict(zip(students, average_grades))

print(grades_dict)

