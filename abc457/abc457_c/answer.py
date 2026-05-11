N, K = map(int, input().split())
L = []
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    L.append(row[0])
    A.append(row[1:])
C = list(map(int, input().split()))
P = 0

for i in range(N):
    P += C[i]*L[i]
    if P >= K:
        j = (K-P+C[i]*L[i-1])%L[i]
        print(A[i][j])
        break