from collections import defaultdict
d=defaultdict(str)
d['purple']='Power'
d['green']='Time'
d['blue']='Space'
d['orange']='Soul'
d['red']='Reality'
d['yellow']='Mind'

n=int(input())
l=[]
for i in range(n):
    l.append(input())

print(6-n)

if n==0:
    for i in d.values():
        print(i)
elif n<6:
    for i in d:
        if i not in l:
            print(d[i])
