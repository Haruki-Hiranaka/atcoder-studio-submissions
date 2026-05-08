T = input()
ans = []
best = 0.0

def valid_input(S):
    return S[0] == "t" and S[-1] == "t"

for size in range(3, len(T)+1):
    for start in range(len(T)-size+1):
        sub = T[start:start+size]

        if valid_input(sub):
            cnt = 0
            cnt = sub[1:-1].count("t")
            best = max(best, cnt/(len(sub)-2))

if best:
    print(best)
else:
    print(0)