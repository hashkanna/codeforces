n=int(input())
a=list(map(int, input().split()))
b=min(a)

min_val=1+(10**9)
prev_ind=a.index(b)
for i in range(prev_ind+1,len(a)):
    if a[i]==b:
        ind=i
        if ind-prev_ind < min_val:
            min_val=ind-prev_ind
        prev_ind=ind
print(min_val)
