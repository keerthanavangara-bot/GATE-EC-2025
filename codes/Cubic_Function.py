import numpy as np
from plot_utils import plt, savefig
def f(x): return 2*x**3-3*x**2-12*x+1
x=np.linspace(-3.5,4,1200)
y=f(x)
print("f'(x)=6(x-2)(x+1); critical points x=-1 and x=2.")
print(f"f(-1)={f(-1)}, f(2)={f(2)}. Cubic is unbounded above and below, so has no global extrema.")
fig,ax=plt.subplots(figsize=(8,5))
ax.plot(x,y,label=r"$f(x)=2x^3-3x^2-12x+1$")
ax.scatter([-1,2],[f(-1),f(2)],zorder=3)
ax.annotate("x=-1",( -1,f(-1)),xytext=(-2.5,8),arrowprops={"arrowstyle":"->"})
ax.annotate("x=2",(2,f(2)),xytext=(2.4,-18),arrowprops={"arrowstyle":"->"})
ax.axhline(0,color="black",lw=.7); ax.axvline(0,color="black",lw=.7)
ax.set(xlabel="x",ylabel="f(x)",title="Q25 — Cubic function and stationary points")
ax.grid(True,alpha=.3); ax.legend()
savefig(fig,"Q25_Cubic_function.png")
