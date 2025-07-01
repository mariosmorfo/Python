def is_square(length: int, width: int) -> bool:
  """
  Checks if a rectangle is a square.

  Args:
    length (int): The length of the rectangle
    width (int): The width or the rectagle

    Returns:
      bool: True if the rectangle is square, False otherwise
  """

  return width == length

def main():
    
    length = 0
    width = 0

    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
    except ValueError:
       print("Invalid input. Please enter two digits")    
       return

    if is_square(length, width):
      print("The rectangle is square.")
    else:
      print("The rectangle is not square")

if __name__ == "__main__":
  main()