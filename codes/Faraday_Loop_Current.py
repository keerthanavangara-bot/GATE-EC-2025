# Q65 text: loop area=5 m^2, B(t)=0.5t Tesla, field perpendicular to loop.
# |emf| = A |dB/dt| = 5*0.5 = 2.5 V. Resistor values are only visible in the figure.
R1=float(input("Enter first resistor value from Q65 figure (ohms): "))
R2=float(input("Enter second resistor value from Q65 figure (ohms): "))
Rtot=R1+R2
emf=5*0.5
print(f"Induced emf magnitude = {emf:.2f} V")
print(f"Current magnitude = emf/(R1+R2) = {emf/Rtot:.6g} A")
