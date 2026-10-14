from itertools import combinations
balls=["R1","R2","B1","B2"]
pairs=list(combinations(balls,2))
good=[p for p in pairs if p[0][0] != p[1][0]]
print("All equally likely pairs:",pairs)
print("Different-colour pairs:",good)
print(f"P(different colours)={len(good)}/{len(pairs)}={len(good)/len(pairs):.6f}")
