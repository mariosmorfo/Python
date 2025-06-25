items = [1, 2, 3, 3.14, True, "CF7"]

for item in items:
  print(item, end=" ")
print()

nested_list = [
    [1,2],
    [3,4],
    [5,6]
]

# nested_list = [[1,2], [3,4], [5,6]]

print(f"first list item: {nested_list[0]}")

# i want to get 3
print(nested_list[1][0]) # 3


#[3,4], [1,2]
print(nested_list[1], nested_list[0], sep=", ")


 