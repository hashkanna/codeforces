def count_div(A, B, K):
    cnt=0
    diff=abs(A-B)+1
    if A%K==0:
        cnt+=1
        print('A',cnt)
        diff-=1
    if B%K==0:
        cnt+=1
        print('B',cnt)
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

A=1
B=3
K=2
print(count_div(A,B,K))
