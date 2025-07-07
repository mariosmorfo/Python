import string
import random

# string to list
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

def generate_password():
  """
  Generate a random password based on the user-specified lenght
  """

  try:
      password_length = int(input("Give the password length: "))

      if password_length <= 0 :
         print("Password must be positive number")
         return
  except ValueError:
     print("Invalid input. Please provide a positive number")
     return
  
  random.shuffle(characters)
  password = []

  for i in range(password_length):
     password.append(random.choice(characters))

  random.shuffle(password)

  #list to string
  password = "".join(password)

  print(f"Generated password: {password}")

def main():
  while True:
     option = input("Do you want to create a password? ('y', 'n' or 'q' for Quit) :")
     if option.lower() == 'y':
        generate_password()
     elif option.lower() == "q":
      print("Goodbye")
      break
     else:
        print("Wrong input")



if __name__ == "__main__":
  main()