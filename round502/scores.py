n=int(input())
rank=1
val=sum(list(map(int, input().split(' '))))
for _ in range(n-1):
    val1=sum(list(map(int, input().split(' '))))
    if val1>val:
        rank+=1
print(rank)
