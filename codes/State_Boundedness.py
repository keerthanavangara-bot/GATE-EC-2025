import numpy as np
A=np.diag([2.,-2.,0.])
B=np.ones((3,1))
print("A eigenvalues:",np.linalg.eigvals(A))
print("Positive eigenvalue +2 makes x1 unstable; bounded input u(t)=1 can drive x1 unbounded.")
print("The stable state can remain bounded for bounded input; the zero eigenvalue state integrates input and can also grow unbounded.")
print("Thus there exists a bounded input for which at least one state is unbounded.")
