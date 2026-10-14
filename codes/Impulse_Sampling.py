import numpy as np
from plot_utils import plt, savefig
# Illustrative band-limited Gaussian-like signal; sample impulses occur at tau+nTs.
Ts=.25; tau=.07; wc=2*np.pi
t=np.linspace(-2,2,4000)
f=np.sinc(2*t) # illustrative only, band-limited shape
sample_times=np.arange(-3,4)*Ts+tau
sample_vals=np.sinc(2*sample_times)
fig,ax=plt.subplots(figsize=(8,4.5))
ax.plot(t,f,label="illustrative f(t)")
ax.stem(sample_times,sample_vals,linefmt="C1-",markerfmt="C1o",basefmt=" ",label="samples at τ+nTs")
ax.set(xlabel="t",ylabel="Amplitude",title="Q38 — Shifted impulse sampling (illustration)")
ax.grid(True,alpha=.3); ax.legend()
savefig(fig,"Q38_Impulse_sampling.png")
print("Sampling theorem: Ts < π/ωc avoids spectral overlap; the offset τ yields reconstructed f(t−τ).")
