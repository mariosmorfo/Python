from typing import List, Tuple, Dict, Optional

# products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
# criteria = {"brand": "lenovo", "price": 100}

def get_result(products, **kwargs):
    
    """
    Filter a list of products based on give keyword arguments
    Each keyword arguments corresponds to a product attribute

    Params:
        products(list[Tuple[str, int]]): A list of tumples where each tuple contains a brand and a price
        **kwargs: (Dict[str, | int]): Arbitary keyword arguments for filtering.
    """
    results = [
  
      (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') >= price
    ]
    return results

def main():
    products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
    criteria = {"brand": "lenovo", "price": 100}

    print(get_result(products, **criteria))



if __name__ == "__main__":
  main()