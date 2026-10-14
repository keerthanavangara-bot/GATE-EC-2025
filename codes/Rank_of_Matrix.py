import numpy as np
A_base = np.array([[2,3,4,5],[0,6,7,8],[0,0,0,0],[0,0,0,0]], dtype=float)
cases = {
    "(i)": (0, 2, 2),
    "(ii)": (0, 0, 0),
    "(iii)": (2, 0, 0),
    "(iv)": (2, 2, 2),
}
for name, (alpha,beta,gamma) in cases.items():
    A=A_base.copy(); A[2,2]=alpha; A[2,3]=beta; A[3,3]=gamma
    print(f"{name}: alpha={alpha}, beta={beta}, gamma={gamma}; rank={np.linalg.matrix_rank(A)}")
