# name
class student:

  def__init__(self, name, roll_number, cgpa):
  self.name = name 
  self.roll_number = roll_number
  self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(students_list, key=lambda student: student.cgpa,reverse=True)
   return sorted_students

students = [
  Student("Mouni", "A123", 7.8),
  Student("Suwathi", "A124", 8.9), 
  Student("Miru","A125",9.2),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA:,.format(student.name, student.roll_number, student.cgpa))