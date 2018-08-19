T=int(input())
for i in range(T):
    n=int(input())
    a=input()
    flag=0
    for j in range(n//2):
        val = abs(ord(a[j])-ord(a[-j-1]))
        if val!=2 and val!=0:
            flag=-1
            break
    if flag==0:
        print("YES")
    else:
        print("NO")
