numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(type(even_numbers))

for num in even_numbers:
  print(num, end= " ")
print()

for num in even_numbers:
  print(num, end= " ")
print()