n=int(input())
a=list(map(int, input().split(' ')))
e=sum(a)//2

L=[]
L_val=0

for i in a:
    if i+L_val<=e:
        L_val+=i
        L.append(i)
    else:
        break

R=[]
R_val=0

for i in a[::-1]:
    if i+R_val<=e:
        R_val+=i
        R.append(i)
    else:
        break
R=R[::-1]

M=a[len(L):n-len(R)]
# print(L, M, R)

SL=sum(L)
SR=sum(R)

while (SL!=SR) and (len(L)!=0) and (len(R)!=0):
    while SL>SR:
        a=L.pop()
        SL-=a
    while SR>SL:
        b=R.pop(0)
        SR-=b
# print(L,M,R)
# print(sum(L), sum(R))
if SL==SR:
    print(SL)
else:
    print(0)
