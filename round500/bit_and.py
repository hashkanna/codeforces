n,x=list(map(int, input().split(' ')))
a=list(map(int, input().split(' ')))

flag=0
if len(set(a))<len(a):
    print(0)
else:
    aa=[]
    for z in a:
        val=z&x
        if val in a and val!=z:
            print(1)
            flag=-1
            break
        aa.append(val)
    if flag==0:
        if len(set(aa))==len(a):
            print(-1)
        else:
            print(2)
