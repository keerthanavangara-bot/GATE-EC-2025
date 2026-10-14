import sympy as sp
s,Ki,Kp,Kd=sp.symbols("s Ki Kp Kd", positive=True, real=True)
# G(s)=1/(10 s^2), unity negative feedback.
char_I=sp.expand(10*s**3+Ki)
char_PD=sp.expand(10*s**2+Kd*s+Kp)
print("Integral controller characteristic polynomial:",char_I)
print("Its s^2 coefficient is zero, so it cannot be Hurwitz stable.")
print("PD controller characteristic polynomial:",char_PD)
print("For Kp>0, Kd>0, all coefficients are positive and second-order Hurwitz condition holds.")
