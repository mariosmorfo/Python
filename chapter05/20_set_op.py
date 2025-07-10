def main():
  store_a_products = {"Apples", "Bananas", "Cherries", "Watermelons"}
  store_b_products = {"Bananas", "Cherries", "Figs", "Grapes", "Melons"}

  # Find common products (intersection) avaliable in both stores
  common_products = store_a_products & store_b_products
  print(common_products)

  #alternative way
  common_products2 = store_a_products.intersection(store_b_products)
  print(common_products2)

  #find all unique products (union) across both stores (A and B)
  all_products = store_a_products | store_a_products
  print(all_products)

  #using func
  all_products2 = store_a_products.union(store_b_products)
  print(all_products2)

  # Find products avaible in store B not in store A
  store_b_exclusive = store_b_products - store_a_products
  print(store_b_exclusive)
  #using func
  store_b_exclusive2 = store_b_exclusive.difference(store_a_products)
  print(store_b_exclusive2)

  # Fing products that are in either Store A or Store B but not in both
  unique_to_eithe_store = store_a_products ^ store_b_products
  print(unique_to_eithe_store)
  # using func
  unique_to_eithe_store2 = store_a_products.symmetric_difference(store_b_products)
  print(unique_to_eithe_store2)


if __name__ == "__main__":
  main()