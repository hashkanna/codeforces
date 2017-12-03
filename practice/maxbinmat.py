n,k=list(map(int, input().split()))
if n<k:
    print(-1)
else:
    a=[[0 for i in range(n)] for j in range(n)]
    for i in range(k):
        a[i][i] = 1
    for i in range(n):
        print(*a[i])
