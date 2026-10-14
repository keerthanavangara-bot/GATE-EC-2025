print("Interval [2,8] has length 6. If m <= f(x) <= M, then 6m <= integral_2^8 f(x)dx <= 6M.")
print("Check each option against beta <= 6m and alpha >= 6M (assuming m,M are nonnegative).")
for label,beta_factor,alpha_factor in [("A",5,7),("B",6,5),("C",7,6),("D",7,5)]:
    valid=(beta_factor<=6 and alpha_factor>=6)
    print(f"({label}) beta={beta_factor}m, alpha={alpha_factor}M -> {'guaranteed' if valid else 'not guaranteed'}")
