l,r,a=list(map(int,input().split()))
diff=abs(l-r)
if diff<=a:
    res=diff+min(l,r)+((a-diff)//2)
else:
    res=a+min(l,r)
print(2*res)
