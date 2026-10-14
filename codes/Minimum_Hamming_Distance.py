import itertools, numpy as np
G=np.array([[1,0,0,1,0,1],[0,1,0,0,1,1],[0,0,1,1,1,0]],dtype=int)
words=[]
for u in itertools.product((0,1),repeat=3):
    c=np.array(u)@G % 2
    words.append((u,"".join(map(str,c)),int(c.sum())))
print("Input -> codeword | Hamming weight")
for u,c,w in words: print("".join(map(str,u)),"->",c,"|",w)
d=min(w for u,c,w in words if any(u))
print("d_min =",d)
