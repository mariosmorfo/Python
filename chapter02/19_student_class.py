class Student:
  """
  A class represents a student with a first name and a last name.

  Attrs:
    firstname (str): The first name of the student
    lastname (str): The last name of the student
  """
  def __init__(self, firstname: str, lastname: str):
    self.firstname = firstname
    self.lastname = lastname

def main():
  st = Student("Bob", "M")
  print(f"Firstname: {st.firstname}")
  print(f"Lastname:{st.lastname}")

if __name__ == "__main__":
  main()