def my_add(*args : int) -> int:
  return sum(args)


def my_avg(*args: int) -> float:
  if not args:
    return 0
  else: 
    return sum(args) / len(args)

def main():
  ages = [10, 20, 30, 55]

  print(my_avg(*ages))
  print(my_add(*ages))

if __name__ == "__main__":
  main()
