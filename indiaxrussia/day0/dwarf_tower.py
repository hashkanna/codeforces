from collections import defaultdict

# def cost(item,c,d):
#     price=c[item-1]
#     for elem in d[item]:
#         price=min(price, cost(elem[0],c,d)+cost(elem[1],c,d))
#     return price



n,m=list(map(int, input().split()))
c=list(map(int, input().split()))
d=defaultdict(list)
mm=[]
cc=[x for x in c]

for i in range(m):
    a1,a2,a3=list(map(int, input().split()))
    cc[a1-1]=min(cc[a1-1], cc[a2-1]+cc[a3-1])
    print(cc)
    # mm.append([[a1-1],[a2-1,a3-1]])

# print(cost(1,c,d))
print(cc[0])
# for i in mm:s
