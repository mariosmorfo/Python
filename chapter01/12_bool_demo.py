a = True

b = False

print(type(a), b, sep=",")
print(type(b), b, sep=",")

#Short circuit
result = a or b
print(result)