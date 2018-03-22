
def energy(k,d,t):
    if k==d:
        return t
    if k>d and k%d==0:
        return t
    # if k>d:
    i=k
    count=k
    switch='off'
    while(i<t):
        if (i%d==0):
            i+=k
            count+=k
        else:
            diff = d-(i%d)
            count += diff/2
            i+=(diff)
    return count


k,d,t=list(map(int, input().split(' ')))
print(energy(k,d,t))
