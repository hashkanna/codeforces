from collections import deque
s=input()
a=deque()
b=deque()
for ind,i in enumerate(s):
    a.append(ind+1) if i=='0' else b.append(ind+1)

print(len(a),len(b))

flag=0
final=[]
c=deque()
while(b and c.extend(a) and flag!=-1):
    res=[]
    aa=a.popleft()
    bb=b.popleft()
    if bb<aa:
        flag=-1
        break
    res.append(aa)
    res.append(bb)
    aa=a.popleft()
    bb=b.popleft()
    while(aa<res[-1] and a and flag!=-1):
        c.append(aa)
        if (not a):
            flag=-1
            break
        else:
            aa=a.popleft()
    if flag==-1:
        break
    if aa>res[-1]:
        res.append(aa)
    if (not a):
        final.append(res)

if flag!=-1 and (c.extend(a)):
    for i in c.extend(a):
        l=[]
        l.append(i)
        final.append(l)

print(final)
if flag==-1:
    print(-1)
else:
    for i in final:
        print(len(final), ' '.join([str(x) for x in i]))
