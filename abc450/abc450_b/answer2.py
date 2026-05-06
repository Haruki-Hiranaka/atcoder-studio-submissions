N = int(input())
C = [[0]*(_+1) + list(map(int, input().split())) for _ in range(N-1)]

def solve(N, C):
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if C[a][c] > C[a][b] + C[b][c]:
                    print("Yes")
                    return 1
    else:
        print("No")
        return 0

solve(N, C)