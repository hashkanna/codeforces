def gar(k1,k2,k3):
    val=k1*k2*k3
    for i in range(1,1501):
        for j in range(1,1501):
            for k in range(1,1501):
                x1=list(range(i,val,k1))
                x2=list(range(j,val,k2))
                x3=list(range(k,val,k3))
                max_val=max(i,j,k)
                x=set(list(range(max_val, val+1)))
                y=set(x1+x2+x3)
                if x==y:
                    return "YES"
    return "NO"

k1,k2,k3=list(map(int, input().split()))
print(gar(k1,k2,k3))
