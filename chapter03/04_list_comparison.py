def compare_list(list1:list, list2: list):
  """
  Compares two list for identity and equality.

  Args:
    list1 (list): First list compare
    list2 (list): Second list compare

    Return: 
      None
  """
  # identity check -> list1 is list2
  print(f"{list1} is {list2} : {list1 is list2}")

  #equality check -> list1 == list2
  print(f"{list1} == {list2}: {list1 == list2}")
  pass

def main():
    my_list = [1, 2, 3]
    your_list = [1, 2, 3]

    #compare lists
    compare_list(my_list, your_list)
    print(id(my_list))
    print(id(your_list))


if __name__ == "__main__":
  main()