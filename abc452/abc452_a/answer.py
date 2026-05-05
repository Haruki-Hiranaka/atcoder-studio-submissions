M, D = map(int, input().split())

if M == 1 and D == 7:
    print("Yes")
elif M in (3, 5, 7, 9) and M == D:
    print("Yes")
else:
    print("No")
    