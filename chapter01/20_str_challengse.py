# challenge 1
#F
#aa
#ccc
#....
#(Factory)

message1 = "Factory"

for i in range(len(message1)):
    print(message1[i] * (i + 1))

# challenge 2
#F******
#aa*****
#ccc****
#tttt***
#rrrrr**
#yyyyyy*
#(Factory)

for i in range(len(message1)):
    print(message1[i] * (i + 1), end="*" * (len(message1) - i - 1))
    print()