N, T = map(int, input().split())
A = list(map(int, input().split()))
total = 0
open_time = 0

A.append(T)
for ai in A:
    if ai > open_time:
        total += (ai - open_time)
        open_time = ai + 100
print(total)