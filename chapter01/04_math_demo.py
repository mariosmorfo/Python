import math

name = "Alice"
age = 20

print("CF7")
print("PI:", math.pi)

print("String concatenation")
# print(name + "is " + age + " years old") Wrong

print(name + "is " + str (age) + " years old")

#Python 2 Style
print()
print("Python 2 Style")
print("PI = %6.1f" %math.pi )
print("%s is %d years old" %(name, age))

print("\nPython 3 Style")

print("Age is {0:2d}".format(age))
print("PI is {0:.3f}".format(math.pi))

print("{0} is {1} years old".format(name, age), end="**")

#f - strings
print(f"{name} is {age} years old")