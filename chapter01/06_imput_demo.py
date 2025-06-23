name = input("Please insert your name: ")

age = int (input("Please enter your age: "))

height = float(input("Please insert your height: "))

is_student = input("Are you student? (YES/NO)").lower() == "yes" #(YES, Yes, yES, yes)

print(f"Hello {name}")

if is_student: 
  print("You are student")
else:
  print("You are not a student")

print("Your age is {} and your height is {:.2f} meters".format(age, height))