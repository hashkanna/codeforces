n=int(input())
a=list(map(int, input().split()))
a=sorted(a)
print(a[((1+n)//2)-1])
