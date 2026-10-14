# The component values/topology in the Q34 figure are required; text alone is insufficient.
# For a standard series-RLC band-pass, bandwidth Δf = R/(2πL), and f_H=f_L+Δf.
fL=1e6
print("Q34: standard series-RLC band-pass helper")
print("If the figure is a series-RLC band-pass, enter its R and L values from the diagram.")
R=float(input("R in ohms: "))
L=float(input("L in henries: "))
bw=R/(2*3.141592653589793*L)
print(f"Bandwidth = {bw/1e6:.6g} MHz")
print(f"Upper -3 dB frequency = {(fL+bw)/1e6:.6g} MHz (round: {round((fL+bw)/1e6)} MHz)")
