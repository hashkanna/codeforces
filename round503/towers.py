n,h,a,b,k=list(map(int,input().split(' ')))

for i in range(k):
    ta,fa,tb,fb=list(map(int,input().split(' ')))
    if ta==tb:
        ans=abs(fa-fb)
    else:
        if (fa>=a and fa<=b) or (fb>=a and fb<=b):
            ans=abs(ta-tb) + abs(fa-fb)
        else:
            ans=abs(ta-tb)
            ans+=min(abs(fa-a)+abs(fb-a), abs(fa-b)+abs(fb-b))
    print(ans)
