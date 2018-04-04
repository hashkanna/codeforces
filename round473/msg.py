n,k,m=list(map(int,input().split(' ')))
w=input().split(' ')
ww={j:i for i,j in enumerate(w)}
c=list(map(int,input().split(' ')))

cost=0
xx=[]
for i in range(k):
    x=list(map(int,input().split(' ')))
    min_val=min([c[j-1] for j in x[1:]])
    for j in x[1:]:
        c[j-1] = min_val
m=input().split(' ')
mm=[c[ww[i]] for i in m]
print(sum(mm))
