import numpy as np
from plot_utils import plt, savefig
p=np.array([[.06,.14],[.24,.56]]) # rows X=0,1; columns Y=0,1
px=p.sum(axis=1); py=p.sum(axis=0)
I=0.
for x in range(2):
    for y in range(2):
        I += p[x,y]*np.log2(p[x,y]/(px[x]*py[y]))
print("P(X):",px,"P(Y):",py)
print(f"I(X;Y)={I:.8f} bits")
fig,ax=plt.subplots(figsize=(6,4.5))
im=ax.imshow(p,origin="lower",vmin=0,vmax=p.max())
for x in range(2):
    for y in range(2): ax.text(y,x,f"{p[x,y]:.2f}",ha="center",va="center")
ax.set(xticks=[0,1],yticks=[0,1],xlabel="Y",ylabel="X",title="Q60 — Joint PMF P(X,Y)")
fig.colorbar(im,ax=ax,label="Probability")
savefig(fig,"Q60_Joint_PMF.png")
