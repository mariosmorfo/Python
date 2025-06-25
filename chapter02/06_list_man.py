fruits = ["Apple", "Banana", "Cherry", "Apple"]

print(f"Initial list: {fruits}")

# Add a fruit in list
fruits.append("Mango")
print("After adding Mango", fruits)


# Add more than 1
fruits.extend(["Grapes", "Fing"])
print("After adding Grapes, fig", fruits)

#Insert an element in a specific position
fruits.insert(1 , "Coconut")
print("After adding Coconut", fruits)

#Update
fruits[0] = "Mellon"
print("After updating", fruits)

#Update a slice of list (two elements)
fruits[1:3] = ["A", "B", "C"]
print("After slicing", fruits)

# pop()
removed_item = fruits.pop(2)
print(f"Removed item:, {removed_item}")
print("After pop", fruits)

#remove
fruits.remove("C")
print("Update after remove('C')", fruits)

idx = fruits.index('A')
print(idx)

item_to_remove = "Grapes"

if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"{item_to_remove} removed")
else: 
    print("insert a valid fruit")