N, T = map(int, input().split())
A = list(map(int, input().split()))
total = 0
now = 0

if len(A) != 0:
    A.append(T)
    for ai in A:
        if ai > now:
            total += (ai - now)
            now = ai+100
    print(total)
else:
    print(T)