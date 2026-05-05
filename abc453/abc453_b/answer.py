T, X = map(int, input().split())
A = list(map(int, input().split()))

print(0, A[0])
last_val = A[0]


for i in range(1, T + 1):
    if abs(last_val - A[i]) >= X:
        print(i, A[i])
        last_val = A[i]
