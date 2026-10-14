import numpy as np
a=np.array([1.,1.]); b=np.array([0.,3*np.sqrt(2)])
xstar=float(a@b/(a@a))
res=xstar*a-b
print(f"x* = a^T b / a^T a = {xstar:.6f}")
print(f"minimum Euclidean norm = ||x*a-b|| = {np.linalg.norm(res):.6f}")
print("Expected value ≈ 3.00.")
