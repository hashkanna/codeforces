n = int(input())
a = list(map(int,input().split()))
s,f = list(map(int,input().split()))

max_val=0
for i in range(n+1-(f-s)):
    val=sum(a[i:i+(f-s)])
    if val > max_val:
        max_val=val
        index_val=i
print(index_val+(f-s)+s-1)
