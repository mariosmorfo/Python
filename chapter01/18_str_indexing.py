message = "Coding Factory"

print(message[0])


print(f"Lenght of {message} = {len(message)}")

for char in message:
    print(char, end =" ")


for i in range(10 + 1):
  print(i)

# print("--------------")

# #for indexing based
# message = "Coding Factory"

# for i in range(len(message)):
#   print(message[i], sep=" ")

my_num = 123456789

str_num = str(my_num)
first_num = int(str_num[0])
last_num = int(str_num[-1])
result = first_num + last_num
print(result)

print(f"Result = {int(str_num[0]) + int(str_num[-1])}")