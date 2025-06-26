def say_hello(name:str = "Coding Factory"):
    """
    Print a message.

    Args:
        name (str): The name to greet. Default value 'Coding Factory'
    """
  #pass
    print(f"Hello {name}")

def main():
  #say_hello("Panos")
  say_hello()
  say_hello("Panos")
  say_hello()

  #.__doc__ for printing documentation
  print(say_hello.__doc__)
  pass

if __name__ == "__main__":
    main()