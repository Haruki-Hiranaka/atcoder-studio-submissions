from itertools import permutations

mat = [list(map(int, input().split())) for _ in range(3)]

counts = []
for i in range(3):
    c = {4: 0, 5: 0, 6: 0}
    for v in mat[i]:
        if v in c:
            c[v] += 1
    counts.append(c)

ans = 0.0
for perm in permutations([4, 5, 6]):
    # perm[i] = サイコロi が出すべき値
    p = 1.0
    for i in range(3):
        p *= counts[i][perm[i]] / 6
    ans += p

print(ans)