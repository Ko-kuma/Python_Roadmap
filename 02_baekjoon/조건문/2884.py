A, B = map(int, input().split())
if B - 45 < 0:
    A -= 1
    B = 60 + (B - 45)
    if A < 0:
        A = 23
    print(A, B)
else:
    print(A, B - 45)
