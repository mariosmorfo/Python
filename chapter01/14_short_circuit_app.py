username = input("Please enter your username: ")
email = input("Please enter your email: ")

valid_user = username or "User"


"""
if email:
  print(f"Hello {valid_user}, your email is: {email}")
else:
  print(f"Hello {valid_user}, please provide your email")

"""

print(f"Hello {valid_user}," + ((email and f"your email is {email}") or ("please provide your email")))