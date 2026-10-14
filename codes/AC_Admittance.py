import cmath, math
# Enter branch admittances Y_C, Y_L, Y_R and source phasor V from the figure.
# Text extraction omits the circuit labels/values, so this is a reusable phasor calculator.
def polar(z):
    return (abs(z), math.degrees(cmath.phase(z)))
print("Q20 AC branch-current calculator")
print("Enter complex admittances as real and imaginary parts in Siemens.")
V=complex(float(input("Source voltage real part (V): ")),float(input("Source voltage imaginary part (V): ")))
for name in ("C","L","R"):
    y=complex(float(input(f"Y_{name} real (S): ")),float(input(f"Y_{name} imaginary (S): ")))
    i=V*y
    mag,ang=polar(i)
    print(f"i_{name} = {mag:.6g} ∠ {ang:.6g}° A (rectangular {i})")
