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

#Delete: remove the 'last' inserted item with popitem()
key, value = products.popitem()
print(f"Key:{key}, Value:{value}")

print(products)

key_to_check=2

if key_to_check in products:
    print(f"Key: {key_to_check} exists")
else:
    print(f"Key: {key_to_check} does not exists")

# iterate
for key in products.keys():
    print(key, ":", products[key])

for values in products.values():
  print(values)

for key, value in products.items():
    print(f"{key}:{value}")
