w,h=list(map(int, input().split()))
w1,h1=list(map(int, input().split()))
w2,h2=list(map(int, input().split()))

while h!=0:
    w+=h
    if h==h1:
        w-=w1
    elif h==h2:
        w-=w2
    if w<0: w=0
    h-=1

print(w)
