ages = [25, 27, 29, 31, 31]
print("Initial list of ages:", ages)

for age in ages:
    print(age, end=" ")
print()

for index, value in enumerate(ages):
    print(f"Index: {index}, Value: {value}")