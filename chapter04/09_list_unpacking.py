my_list = [1, 2, 3, 4, 5]

#simple unpacking
a, b, c, d, e = my_list

print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")


# skipping some values
a, _b, c, _d, e = my_list
print(f"a = {a}, c = {c}, e = {e}")

#unpack the first element, and the lasts
a, *b = my_list
print(f"a = {a}, b = {b}")

a, *b, c = my_list
print(f"a = {a}, b = {b}, c = {c}")




