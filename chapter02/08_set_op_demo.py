bag = {"eggs", "oranges", "bananas"}
print("Initial bag", bag)

#add a new item
bag.add("Grapes")
print("Bag after adding Grapes", bag)

# #remove
# bag.remove("melon")
# print("Bag after remove bananas", bag)

for item in bag:
    print(item, end=" ")
print()