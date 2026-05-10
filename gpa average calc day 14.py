def student_grades(student_name, student_grades):
  try:
    grade_average = round(sum(student_grades) / len(student_grades), 2)
    
    grade_data = {'Name': student_name, 
                  'Grades': student_grades,
                  'Gpa': grade_average}
    return grade_data
  
  except TypeError:
    print('Error occured')

result = student_grades('Julien', [84, 70, 70, 79, 84, 100, 67, 55, 55])
for key , value in result.items():
    print(f'{key}: {value}')
  
