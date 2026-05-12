N = int(input())
L = []
A = []
for i in range(N):
    row = list(map(int, input().split()))
    L.append(row[0])
    A.append(row[1:])
X, Y = map(int, input().split())

print(A[X-1][Y-1])