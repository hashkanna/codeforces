from collections import Counter
import operator

n=int(input())
a=input()
b=input()
c=input()

aa=max(Counter(a).items(), key=operator.itemgetter(1))[1]
bb=max(Counter(b).items(), key=operator.itemgetter(1))[1]
cc=max(Counter(c).items(), key=operator.itemgetter(1))[1]


res=[len(a)-aa, len(a)-bb, len(a)-cc]

newres=[]
for i in res:
    if i <= n:
        newres.append((n-i)%2)
    else:
        newres.append(i-n)
# print(res)
# print(newres)

if newres.count(min(newres))>1:
    print('Draw')
else:
    if min(newres) == newres[0]:
        print('Kuro')
    elif min(newres) == newres[1]:
        print("Shiro")
    else:
        print("Katie")
