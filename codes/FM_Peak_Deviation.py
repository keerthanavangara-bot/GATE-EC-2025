import numpy as np
from plot_utils import plt, savefig
# phi(t)=2*pi*fc*t + 3 sin(2*pi*f1*t) + 4 sin(6*pi*f1*t)
# fi(t)=fc + (1/2pi) d(phi_extra)/dt = fc + 3*f1*cos(2pi f1 t)+12*f1*cos(6pi f1 t)
x=np.linspace(0,1,4000,endpoint=False) # x=f1*t
delta=3*np.cos(2*np.pi*x)+12*np.cos(6*np.pi*x)
peak=np.max(np.abs(delta))
print(f"Peak frequency deviation = {peak:.6g} * f1 (numerical; exact maximum can be checked analytically)")
fig,ax=plt.subplots(figsize=(8,4.5))
ax.plot(x,delta)
ax.axhline(peak,ls="--",label=f"max |deviation| ≈ {peak:.3f} f1")
ax.axhline(-peak,ls="--")
ax.set(xlabel=r"$f_1 t$",ylabel=r"$f_i(t)-f_c$ (Hz)",title="Q14 — Instantaneous frequency deviation")
ax.grid(True,alpha=.3); ax.legend()
savefig(fig,"Q14_FM_deviation.png")
