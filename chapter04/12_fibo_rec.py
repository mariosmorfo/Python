def fibo(n: int) -> int:
  if n in (0, 1): return n
  return fibo(n-1) + fibo(n-2)

def main():
  n = int(input("Please give an integer"))
  print(f"fibo({n}) = {fibo(n)}")

if __name__ == "__main__":
  main()