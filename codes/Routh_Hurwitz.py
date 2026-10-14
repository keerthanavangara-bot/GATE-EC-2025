import numpy as np
p=[1,7,3,-33,2,-40]
roots=np.roots(p)
L=sum(r.real < -1e-7 for r in roots)
I=sum(abs(r.real)<=1e-7 for r in roots)
R=sum(r.real > 1e-7 for r in roots)
print("Roots:")
for z in roots: print(f"{z.real:+.6f}{z.imag:+.6f}j")
print(f"L={L}, I={I}, R={R}")
