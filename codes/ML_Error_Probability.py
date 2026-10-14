import numpy as np
from plot_utils import plt, savefig
# Three equiprobable symbols -2,0,2; nearest-neighbour thresholds are -1 and +1.
# Error for outer symbols: one tail; error for middle symbol: two tails.
# With symmetry, average Pe = (1/3)P(N>1)+(1/3)2P(N>1)+(1/3)P(N>1)=4/3 P(N>1).
print("alpha = 4/3")
x=np.linspace(-4,4,1000); sigma=1.0
pdf=np.exp(-x*x/(2*sigma*sigma))/(sigma*np.sqrt(2*np.pi))
fig,ax=plt.subplots(figsize=(8,4.5))
ax.plot(x,pdf,label="zero-mean Gaussian noise (illustrative σ=1)")
xx=np.linspace(1,4,300); ax.fill_between(xx,np.exp(-xx*xx/2)/np.sqrt(2*np.pi),alpha=.3,label="P(N > 1)")
ax.axvline(1,ls="--")
ax.set(xlabel="N",ylabel="Density",title="Q41 — Gaussian tail used in ML error probability")
ax.grid(True,alpha=.3); ax.legend()
savefig(fig,"Q41_Gaussian_tail.png")
