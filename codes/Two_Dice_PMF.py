import numpy as np
from collections import Counter
from itertools import product
from plot_utils import plt, savefig
sums=[a+b for a,b in product(range(1,7),repeat=2)]
cnt=Counter(sums); xs=np.arange(2,13); pmf=np.array([cnt[x]/36 for x in xs])
print(f"E[X]={sum(x*p for x,p in zip(xs,pmf)):.2f}")
print("PMF:")
for x,p in zip(xs,pmf): print(f"P(X={x})={p:.6f}")
fig,ax=plt.subplots(figsize=(8,4.5))
ax.bar(xs,pmf,width=.8,edgecolor="black")
ax.set(xticks=xs,xlabel="Sum X",ylabel="P(X=x)",title="Q58 — PMF of the sum of two fair dice")
ax.grid(axis="y",alpha=.3)
savefig(fig,"Q58_Two_dice_PMF.png")
