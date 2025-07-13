numbers = [1, 2, 3, 4, 5, 6, 7]

squared_nums = {num:numbers*2 for num in numbers}
print(squared_nums)

def square(n):
  return n **2

sq_dict = {num: square(num) for num in numbers}
print(sq_dict)