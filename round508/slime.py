n=int(input())
a=list(map(int,input().split(' ')))

if len(a)==1:
    print(a[0])
if len(a)==2:
    print(abs(a[0]-a[1]))
if len(a)>2:
    for i in range(len(a)-2):
        
