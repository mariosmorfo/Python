def get_average(*num):
  """
  ...
  """
  if not num:
     return "Not numbers provided."
  
  average = sum(num) / len(num)
  return "{:.2f}".format(average)


def main():
  num = [10, 30, 40 , 50, 60]
  my_average = get_average(*num)
  print(my_average)

if __name__ == "__main__":
    main()