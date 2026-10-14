import math
# Source vs(t)=100 cos(200t); RMS source = 100/sqrt(2).
# If M1 is across the LTI block output, the given 25 V and 5 A constrain the network.
omega=200.0
L=1.0
R=5.0
Vs_rms=100/math.sqrt(2)
Vload=25.0
I=5.0
Zmag=Vload/I
print(f"Source RMS = {Vs_rms:.4f} V; load |Z| implied by 25 V / 5 A = {Zmag:.4f} ohm.")
print("The circuit includes an unspecified linear time-invariant block, so its output impedance is unknown.")
print("Therefore C is not uniquely inferable from the given meter readings alone.")
