def judge(X):
    return X >= 3 and X <= 18


X = int(input())

if judge(X): print("Yes")
else: print("No")