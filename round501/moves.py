n=int(input())
s1=list(input())
s2=list(input())

from collections import Counter

if Counter(s1)!=Counter(s2):
    print(-1)
else:
    moves=[]
    ind=0
    while len(moves)<10000 and ind<n:
        if s1[ind]==s2[ind]:
            ind+=1
        else:
            t=s1.index(s2[ind])
            del s1[t]
            s1.insert(ind, s2[ind])
            moves+=range(ind+1,t+1)[::-1]
            ind+=1
            print(s1, s2, moves)
    if len(moves)>10000 or s1!=s2:
        print(-1)
        print(len(moves))
    else:
        print(len(moves))
        print(*moves)
