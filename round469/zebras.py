s=input()
a=[ind+1 for ind,i in enumerate(s) if i=='0']
b=[ind+1 for ind,i in enumerate(s) if i=='1']
print(a,b)

i=0
j=0
final=[]
flag=0
while(b!=[] and flag!=-1):
    if len(a)<=len(b) or a[0]>b[0]:
        print(final)
        print(a,b)
        print('kanna1')
        flag=-1
        break
    else:
        res=[]
        res.append(a[0])
        del(a[0])
        while(a!=[] and b!=[] and flag!=-1):
            if b[0] < res[-1]:
                flag=-1
                break
            res.append(b[0])
            del(b[0])
            if a[-1] < res[-1]:
                # print('kanna2')
                flag=-1
                break
            # else:
            #     res.append()
            j=0
            while a!=[] and a[j] < res[-1]:
                j+=1
                # l=[]
                # l.append(a[0])
                # final.append(l)
                # del(a[0])
            if a!=[] and a[j]>res[1]:
                res.append(a[j])
                del(a[j])
        final.append(res)


if b!=[]:
    flag=-1

if a!=[]:
    for i in a:
        l=[]
        l.append(i)
        final.append(l)

if flag==-1:
    print(-1)
else:
    for i in final:
        print(len(i), ' '.join([str(x) for x in i]))
