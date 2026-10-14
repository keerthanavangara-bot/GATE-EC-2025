import numpy as np
from plot_utils import plt, savefig
T=1.0; N=8; t=np.linspace(0,N*T,4000)
# Deterministic illustration with independent-like zero-mean coefficients (seed fixed).
rng=np.random.default_rng(42)
a=rng.normal(size=N)
f=np.zeros_like(t)
for n in range(1,N+1):
    f += a[n-1]*((t >= n*T) & (t <= n*T+.5*T))
print("Mean is zero for every t because E[a_n]=0.")
print("Autocorrelation is not generally time-invariant for this finite, gated pulse train.")
fig,ax=plt.subplots(figsize=(8,4))
ax.plot(t,f)
ax.set(xlabel="t",ylabel="f(t) (one realization)",title="Q42 — Finite gated random pulse train (illustration)")
ax.grid(True,alpha=.3)
savefig(fig,"Q42_Random_process.png")
