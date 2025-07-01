def compare_integers(a, b):
  if a == b:
    print("The numbers are equals")

  elif a > b:
    print("The first number is greater than the second number")
  
  else:
    print("The first number is smaller than the second number")

def main():
  try:
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
  except ValueError:
    print("Invalid input")

  compare_integers(a, b)

  # simple example
  if a > 0:
    print("positive")
  else:
    print("non-positive")

    result = "positive" if a > 0 else "non-positive"
    print(result)

  # extended example
  result = (
      "The numbers are equals." if a == b else
      "The first number is greater than the second number" if a > b else
      "The first number is smaller than the second number"
  )
  print(result)

if __name__ == "__main__":
  main()