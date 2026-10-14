from itertools import product
print("X Y Z | Sum S Carry Cout | S XOR Z")
for X,Y,Z in product((0,1), repeat=3):
    S=X^Y^Z
    C=(X&Y)|(X&Z)|(Y&Z)
    print(X,Y,Z,"|",S,C,"|",S^Z)
print("With Z=1, compare the resulting two-bit output against X-Y modulo 2.")
