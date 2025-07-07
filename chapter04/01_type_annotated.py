def my_add(a: float | int, b: float | int) -> float | int:
  """
  Adds two numbers adn returns the result

  Args:
    a (int, float): The first number to add.
    b (int, float): The second number to add.

    Returns:
      int | float: The sum of 'a' or 'b'.

      Raise:
        TypeError: if either 'a' or 'b' is not an integer or float

  """

  if not (isinstance(a, (int,float)) and isinstance(b, (int, float))):
    raise TypeError("Both must be integers or floats")
  return a + b

def main():
  print(my_add(1, 22.5))

  try:
    print(my_add("Hello" , 10))
  except TypeError as e:
    print(e)

    print("Annotations:", my_add.__annotations__)
    print("Docs:", my_add.__doc__)
    print("-" * 20)
    help(my_add)
  

if __name__ == "__main__":
  main()