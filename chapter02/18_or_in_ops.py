choice = "q"

if choice == 'q' or choice == "Q":
  print("Quiz")
else:
  print("Continue")

if choice.upper() == "Q":
  print("Quiz")
else:
  print("Continue")


  if choice in ('q', 'Q'):
    print("Quit")