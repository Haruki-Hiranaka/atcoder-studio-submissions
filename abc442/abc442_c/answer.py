N, M = map(int, input().split())
ans = list()

deg = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    deg[a] += 1
    deg[b] += 1

for i in range(1, N+1):
    ans.append(str(((N-deg[i]-1) * (N-deg[i]-2) * (N-deg[i]-3))//6))

print(" ".join(ans))