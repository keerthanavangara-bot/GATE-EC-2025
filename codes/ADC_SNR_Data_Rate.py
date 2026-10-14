N=10
fs=1e6
snr=6.02*N+1.76
Rb=fs*N
print(f"Maximum ideal ADC SNR = 6.02N+1.76 = {snr:.2f} dB")
print(f"Output bit rate = fs*N = {Rb/1e6:.2f} Mbps")
print("The input tone at fs/2 does not change the ideal quantization-SNR formula.")
