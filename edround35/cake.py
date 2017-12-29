n,a,b=list(map(int, input().split()))
# if n%2==0:
#     d1=n//2
#     d2=n//2
# else:
#     d1=n//2
#     d2=d1+1
# x=max(a,b) // max(d1,d2)
# y=min(a,b) // min(d1,d2)
# print(min(x,y))

def cake(n,a,b):
    min_val=min(a,b)
    max_val=max(a,b)

    # print(max_val//(n-min_val))
    if max_val//(n-min_val) == min_val:
        return(min_val)
    else:
        for i in range(min_val//2,0,-1):
            if max_val//(n-i) == i:
                return(i)

print(cake(n,a,b))
