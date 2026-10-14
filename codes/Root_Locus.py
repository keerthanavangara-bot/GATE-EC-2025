import numpy as np
from plot_utils import plt, savefig
# Candidate point is s=-1+j. Root-locus angle condition: G(s) must be real negative.
# Use this helper after entering the open-loop transfer function's pole/zero locations from Fig. (i).
poles=input("Enter open-loop poles from Fig. (i), comma-separated real or a+bj (e.g. 0,-2): ").split(",")
zeros=input("Enter open-loop zeros from Fig. (i), comma-separated; blank if none: ").split(",")
def parse(v):
    v=v.strip().replace("i","j")
    return complex(v)
P=[parse(x) for x in poles if x.strip()]
Z=[parse(x) for x in zeros if x.strip()]
s=complex(-1,1)
angle=(sum(np.angle(s-z) for z in Z)-sum(np.angle(s-p) for p in P))
print(f"Angle of G(s) at s=-1+j = {np.degrees(angle):.3f} degrees modulo 360.")
print("Root-locus condition requires angle G(s) = odd multiple of 180 degrees; if satisfied, K=1/|G(s)| times any numerator/denominator gain.")
