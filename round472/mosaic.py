from collections import defaultdict
n,m=list(map(int,input().split()))
d={}
rows=list(range(n))
cols=list(range(m))
for i in range(n):
    s=input()
    d[i]=tuple([ind for ind,i in enumerate(s) if i=='#'])
print(d)
dd=defaultdict(list)
for i in d[i]:
    # x=tuple(d[i])
    x=tuple(i)
    dd[x].append(i)
print(dd)

def check(d,dd,m,n,s,rows,cols):
    tmp=[]
    for i in d:
        # rows.remove(i)
        # for y in d[i]:
        #     if y in cols:
        #         cols.remove(y)
        #     else:
        #         return 'No'
        # if i not in rows:

        #if d[i] in dd:
        # for y in d[i]:
        #     if y in cols:
        #         cols.remove(y)

        if i not in tmp:
            for x in dd[d[i]]:
                if x in rows:
                    # print('kanna', x)
                    rows.remove(x)
                    tmp.append(x)
                    # d=dict((k,v) for k,v in d.items() if k!=x)
                    # print(d)
                    # tmp.append(x)
                else:
                    print(i,d[i])
                    # if x not in tmp:
                    return 'No'
        # del dd[d[i]]
    return 'Yes'

print(check(d,dd,m,n,s,rows,cols))
