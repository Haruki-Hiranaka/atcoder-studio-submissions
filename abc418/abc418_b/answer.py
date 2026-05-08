T = input()
ans = list()

def valid_input(S):
    return S[0] == "t" and S[-1] == "t"

for size in range(3, len(T)+1):
    for start in range(len(T)-size+1):
        S = T[start:start+size]

        if valid_input(S):
            cnt = 0
            for i in range(1, len(S)-1):
                if S[i] == "t":
                    cnt += 1
            ans.append(cnt/(len(S)-2))

if ans:
    print(max(ans))
else:
    print(0)