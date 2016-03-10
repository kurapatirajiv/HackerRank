A = map(int, input.split())
B = map(int, input.split())
C = map(int, input.split())
D = map(int, input.split())
AB = []
BC = []
cD = []
# Combining two individual vectors
AB = AB.append(",".join(p-q for p,q in zip(B, A)))
BC = BC.append(",".join(p-q for p,q in zip(B, A)))
CD = CD.append(",".join(p-q for p,q in zip(B, A)))
