H, W = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]
cnt = 0

for h1 in range(1, H+1):
    for h2 in range(h1, H+1):
        for w1 in range(1, W+1):
            for w2 in range(w1, W+1):
                for i in range(h1, h2+1):
                    flag = True

                    for j in range(w1, w2+1):
                        if grid[i - 1][j - 1] != grid[h1 + h2 - i - 1][w1 + w2 - j - 1]:
                            flag = False
                            break
                    
                    if not flag:
                        break
                else:
                    cnt += 1

print(cnt)