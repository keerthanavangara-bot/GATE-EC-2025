import numpy as np
from plot_utils import plt, savefig
T0=2*np.pi; alpha=2.0
t=np.linspace(0,2*T0,2000)
f=np.cos(2*np.pi*t/T0)+.4*np.sin(4*np.pi*t/T0)
y=np.cos(2*np.pi*alpha*t/T0)+.4*np.sin(4*np.pi*alpha*t/T0)
fig,ax=plt.subplots(figsize=(8,4.5))
ax.plot(t,f,label="f(t)")
ax.plot(t,y,label="y(t)=f(αt)",alpha=.8)
ax.set(xlabel="t",ylabel="Amplitude",title="Q55 — Time scaling compresses the period")
ax.grid(True,alpha=.3); ax.legend()
savefig(fig,"Q55_Fourier_time_scaling.png")
print("For y(t)=f(αt), the fundamental period is T0/α. Fourier-series coefficients are unchanged when indexed by the same harmonic k.")
