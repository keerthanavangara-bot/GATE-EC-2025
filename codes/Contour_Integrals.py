import numpy as np
# Unit circle z=e^(it), dz=i e^(it)dt. Numerical integration confirms entire functions integrate to zero.
t=np.linspace(0,2*np.pi,200001)
z=np.exp(1j*t); dz=1j*z
for name, f in [("exp(z)",np.exp(z)),("cos(z)",np.cos(z)),("z^2",z**2)]:
    val=np.trapz(f*dz,t)
    print(f"Integral of {name} dz ≈ {val.real:.3e} + j{val.imag:.3e}")
print("For integer n, ∮ z^n dz is 2πj only when n=-1; it is 0 otherwise.")
print("sec(z) has poles where cos(z)=0; none lie on or inside |z|=1, so its contour integral is 0 by Cauchy's theorem.")
