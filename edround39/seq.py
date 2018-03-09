n=int(input())
a=list(map(int, input().split()))
a=[abs(i) for i in a]
print(sum(a))
