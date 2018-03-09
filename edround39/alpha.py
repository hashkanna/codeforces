alpha=input()
elem='a'
count=1
ind=alpha.find('a')
res=alpha[:ind+1]
if ind==-1:
    print(-1)
else:
    alpha=alpha[ind+1:]
    for indx,i in enumerate(alpha):
        # print(res)
        if ord(i)<=ord(elem)+1:
            count+=1
            elem=chr(ord(elem)+1)# if ord(i)<=ord(elem)+1 else i
            # print(elem)
            res+=elem
        else:
            res+=i
        if count==26:
            res+=alpha[indx+1:]
            break
    if count==26:
        print(res)
    else:
        print(-1)
