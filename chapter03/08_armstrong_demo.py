def is_armstrong_number(num):
  digits = str(num)
  power = len(digits)
  total = 0

  for digit in digits:
    total += int (digit) ** power

    return num == total

def main():
  try: 
    num = int(input("Please insert an int: "))
  except ValueError:
      print("Invalid input return")

  if is_armstrong_number(num):
    print(f"{num} is armstrong number")
  else:
     print(f"{num} isn't armstrong number")


if __name__ == "__main__":
  main()