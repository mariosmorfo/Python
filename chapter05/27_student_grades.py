students = {
  "Alice": [85, 92, 100],
  "Bob": [40., 70, 70],
  "Charlie": [90, 95, 94],
  "Diana": [95, 98, 100],
  "Eve": [50, 40, 30]
}

def main():
  while True: 
      try:
        threshold = int(input("Please insert a threshold (int): "))
      except ValueError:
        print("Ivalid input.")
        continue

      average_grades = {
         student: round(sum(grades) / len(grades), 2)
         for student, grades in students.items()
         if grades and (sum(grades) / len(grades)) > threshold
      }

      for student, avg_grade in average_grades.items():
         print(f"{student}: {avg_grade}")


if __name__ == "__main__":
    main()
