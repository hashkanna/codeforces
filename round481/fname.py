n=int(input())
a=input()
c=0
i=0
while i+2<n:
    if (a[i]=='x' and a[i+1]=='x' and a[i+2]=='x'):
        c+=1
    i+=1
print(c)
