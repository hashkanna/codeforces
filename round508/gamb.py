n=int(input())
a=sorted(list(map(int,input().split(' '))), reverse=True)
b=sorted(list(map(int,input().split(' '))), reverse=True)

A=0
B=0
while a!=[] or b!=[]:
    if b==[]:
        A+=a[0]
        del(a[0])
        if a!=[]: del(a[0])
    elif a==[]:
        del(b[0])
        if b!=[]:
            B+=b[0]
            del(b[0])
    elif a[0]>=b[0]:
        A+=a[0]
        del(a[0])
        if a==[]:
            B+=b[0]
            del(b[0])
        elif b[0]>=a[0]:
            B+=b[0]
            del(b[0])
        else:
            del(a[0])
    elif b[0]>a[0]:
        del(b[0])
        if b==[]:
            del(a[0])
        elif b[0]>=a[0]:
            B+=b[0]
            del(b[0])
        else:
            del(a[0])
print(A-B)
