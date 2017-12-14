h1,a1,c1=list(map(int,input().split()))
h2,a2=list(map(int,input().split()))
l=[]
while h2>0:
    if a1>=h2:
        l.append('STRIKE')
        h2=h2-a1
    elif h1>a2:
        l.append('STRIKE')
        h2=h2-a1
    else:
        l.append('HEAL')
        h1=h1+c1
    h1=h1-a2

print(len(l))
for i in l:
    print(i)
