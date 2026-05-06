N = int(input())
C = [list(map(int, input().split())) for _ in range(N-1)]

def solve(N, C):
    for a in range(N-2):
        for b in range(N-a-1):
            for c in range(N-b-a-2):
                if C[a][b + c + 1] > C[a][b] + C[a + b + 1][c]:
                    print("Yes")
                    return 1
    else:
        print("No")
        return 0

solve(N, C)