class Student:
  
  def __init__(self, name, roll_number, cgpa):
    self. name = name
    self. roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  
  #Sort the list of students Ln descending order of CGPA
  sorted_students = sorted(student_list,  
                          key=lambda Student: Student.cgpa, 
                          reverse=True)
  return sorted_students
# Exanple usage:
students = [
  Student("ammu", "A123", 7.8),
  Student("ramy","A124", 8.9),
  Student("muru","A125",9.1),
  Student("lucky", "A126", 9.9),
]
sorted_students = sort_students(students)
# Print the sorted tist of students
for student in sorted_students:
   print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                      
student.roll_number,
                                                                     student.cgpa))