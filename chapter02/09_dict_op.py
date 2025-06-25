#populate dict
products = {
  1:"Apple", 
  2:"Banana", 
  3:"Honey", 
  4:"Melon"
}

print(f"Initial dict: {products}")

#insert/update a new key:value pair
products[5] = "orange"
print(f"Dict after insertion: {products}")

# read an element

# product_10 = products[10]
# print(product_10)

product_10 = products.get(10, "Out of stock")
print(product_10)

del products[1]
print(f"After deleting key 1 {products}")

removed_item = products.pop(3)
print(f"removed item: {removed_item}")
print(f"after removal: {products}")