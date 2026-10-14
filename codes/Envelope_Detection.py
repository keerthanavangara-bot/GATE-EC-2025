import numpy as np
from plot_utils import plt, savefig
t=np.linspace(0,4,5000)
fc=8
m=np.cos(2*np.pi*.5*t)
mu=.7
dsb=m*np.cos(2*np.pi*fc*t)
am=(1+mu*m)*np.cos(2*np.pi*fc*t)
fig,axs=plt.subplots(2,1,figsize=(9,6),sharex=True)
axs[0].plot(t,dsb,lw=.8); axs[0].set_title("DSB-SC: envelope is proportional to |m(t)|")
axs[1].plot(t,am,lw=.8); axs[1].set_title("AM: envelope follows 1 + μm(t) when it stays nonnegative")
for ax in axs: ax.grid(True,alpha=.25); ax.set_ylabel("Amplitude")
axs[-1].set_xlabel("Time (s)")
savefig(fig,"Q28_Envelope_detection.png")
print("Statement (i) is false as a general claim: DSB-SC envelope is Ac*|m(t)|, not signed m(t).")
print("Statement (ii) is false as phrased: envelope detection requires 1+mu*m(t) not to change sign, not m(t)>0 itself.")
