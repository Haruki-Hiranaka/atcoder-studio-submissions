N = int(input())
S = input()
cnt = 0

def del_o(N, S, cnt):
    for i in range(len(S)):
        if S[i] != "o":
            return (S[i:])

        else:
            cnt += 1

    if cnt == N:
        return ""

print(del_o(N, S, cnt))