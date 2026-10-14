import numpy as np
from plot_utils import plt, savefig
# Standard reading: 4m x 4m square centred on origin, x,y in [-2,2].
x=np.linspace(-2,2,401); y=np.linspace(-2,2,401)
X,Y=np.meshgrid(x,y)
rho=4*np.abs(Y) # microcoulomb/m^2
Q=np.trapz(np.trapz(rho,x,axis=1),y)
print(f"Numerical charge over [-2,2]x[-2,2] = {Q:.4f} microC; analytic value = 64 microC.")
fig,ax=plt.subplots(figsize=(6,5))
im=ax.contourf(X,Y,rho,levels=20)
fig.colorbar(im,ax=ax,label=r"$\rho_s(x,y)=4|y|$ ($\mu$C/m$^2$)")
ax.set_aspect("equal"); ax.set(xlabel="x (m)",ylabel="y (m)",title="Q49 — Surface charge density over 4 m × 4 m sheet")
savefig(fig,"Q49_Surface_charge_density.png")
