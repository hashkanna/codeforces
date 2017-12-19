n=int(input())
l=list(range(1,n+1))
r=[]

if n%4==0:
    r=list(range(1,n//2,2)) + list(range(n,n//2,-2))
    print(0)
    print(len(r), *r)

if n%4==2 and n!=2:
    r=list(range(1,n//2,2)) + list(range(n,n//2,-2))
    print(1)
    print(len(r), *r)

if n%4==1:
    r=list(range(1,n//2,2)) + list(range(n,n//2,-2))
    # print(r)
    m=(n+1)//2
    if (m//2)%2!=0:
        m=m//2
    else:
        m=(m+1)//2
    r.remove(m)
    print(1)
    print(len(r), *r)

if n%4==3:
    n+=1
    r=list(range(1,n//2,2)) + list(range(n,n//2,-2))
    r.remove(n)
    r.append(n//2)
    print(0)
    print(len(r), *r)

if n==2:
    print(1)
    print(1, 1)
