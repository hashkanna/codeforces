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
while(b and a):
    aa=a.popleft()
    bb=b.popleft()
    if bb<aa:
        flag=-1
        break
    
