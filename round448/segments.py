n,x,k=list(map(int, input().split()))
a=list(map(int, input().split()))

def count_div(A, B, K):
    cnt=0
    diff=abs(A-B)+1
    if A%K==0:
        cnt+=1
        # print('A',cnt)
        diff-=1
    if B%K==0:
        cnt+=1
        # print('B',cnt)
        diff-=1
    # if (A%K!=0 and B%K!=0):
    #     cnt+= abs(B-A)//K
    #     print('C',cnt)
    # else:
    #     cnt+= abs(B-A-1)//K
    #     print('D', cnt)
    cnt+=diff//K
    if K>min(A,B) and B-A != K:
        cnt+=1
    return cnt

# A=4
# B=15
# K=4
# print(count_div(A,B,K))

res=0
if k==0:
    res=n
else:
    for i in range(n):
        for j in range(i,n):
            if count_div(a[i],a[j],x) == k:
                # print(a[i],a[j],x)
                res+=1
            # c=0
            # for m in range(a[i],a[j]+1):
            #     print(m,x)
            #     if m%x==0:
            #         c+=1
            # print('c=', c)
            # if c==k:
            #     res+=1
print(res)

# res=0
# if k==0:
#     res=n
# else:
#     for i in range(n):
#         for j in range(n):
#             c=0
#             for m in range(a[i],a[j]+1):
#                 print(m,x)
#                 if m%x==0:
#                     c+=1
#             print('c=', c)
#             if c==k:
#                 res+=1
#print(res)
