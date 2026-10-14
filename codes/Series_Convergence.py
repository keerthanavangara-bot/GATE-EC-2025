import numpy as np
import math
from plot_utils import plt, savefig
N=250
n=np.arange(1,N+1)
s1=np.cumsum(1/np.sqrt(n))
s2=np.cumsum(1/(n*(n+1)))
s3=np.cumsum(1/np.array([math.factorial(int(k)) for k in n], dtype=float))
fig,ax=plt.subplots(figsize=(8,5))
ax.plot(n,s1,label=r"$\sum 1/\sqrt{n}$ (diverges)")
ax.plot(n,s2,label=r"$\sum 1/[n(n+1)]$ (to 1)")
ax.plot(n,s3,label=r"$\sum 1/n!$ (to $e-1$)")
ax.set(xlabel="N",ylabel="Partial sum",title="Q12 — Partial sums of the three series")
ax.grid(True,alpha=.3); ax.legend()
savefig(fig,"Q12_Series_convergence.png")
print("Result: only (ii) and (iii) converge.")
