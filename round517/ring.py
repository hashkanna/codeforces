w,h,k = list(map(int, input().split(' ')))
res=0
w-=2
for i in range(k):
    #tot=(w-(4*(i-1)))*(h-(4*(i-1)))
    h_val=2*(h-(4*i))
    if h_val<2:
        h_val=0
    elif h_val==2:
        h_val=1
    w_val=2*(w-(4*i))
    if w_val<0:
        w_val=0
    res+= h_val+w_val
print(res)
