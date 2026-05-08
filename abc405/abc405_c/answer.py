N = int(input())
A = list(map(int, input().split()))
total = 0
Sum = sum(A)

for i in range(N-1):
    Sum -= A[i]
    total += A[i]*(Sum)

print(total)