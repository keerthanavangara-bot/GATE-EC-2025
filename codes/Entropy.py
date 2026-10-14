import numpy as np
from plot_utils import plt, savefig
def H(a):
    p=np.array([a,1-2*a,a])
    return -np.sum(p*np.log2(p))
for a in (.4,.3,.25): print(f"H({a})={H(a):.6f} bits")
a=np.linspace(.001,.499,1000); h=np.array([H(v) for v in a])
fig,ax=plt.subplots(figsize=(8,4.5))
ax.plot(a,h,label="H(X)")
for v in (.25,.3,.4): ax.scatter(v,H(v),label=f"α={v}: {H(v):.3f}")
ax.set(xlabel="α",ylabel="Entropy (bits)",title="Q54 — Entropy of {-1,0,1} distribution")
ax.grid(True,alpha=.3); ax.legend()
savefig(fig,"Q54_Entropy.png")
