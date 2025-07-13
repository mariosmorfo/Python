def main():
  students = {
  "Alice": 85,
  "Bob": 40,
  "Charlie": 90, 
  "Diana": 100,
  "Eve": 30
}
  
  # Find the student with the lowest grade
  student_with_min_grade = min(students)
  print(student_with_min_grade)

  # Student with min grade
  student_with_min_grade = min(students, key=students.get)
  print(student_with_min_grade)

  # Student with the shortest name by length
  student_with_shortest_name = min(students, key=len)
  print(student_with_shortest_name)

if __name__ == "__main__":
    main()
