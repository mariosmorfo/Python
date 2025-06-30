def print_id(variable_name, variable):
  print(f"id({variable_name}) = {id(variable)}")
  



def main():
  original_list = [1, 2]
  new_list = original_list

  print("Original_list", original_list)
  print("new_list", new_list)

  print("----------------")

  new_list[0] = 100
  print("Original_list", original_list)
  print("new_list", new_list)

if __name__ == "__main__":
  main()