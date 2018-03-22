R,C=list(map(int, input().split(' ')))
a=[list(input()) for i in range(R)]


def sheep(a,R,C):
    flag=0
    for i in range(R):
        for j in range(C):
            if a[i][j]=='W' and ( (i>0 and a[i-1][j]=='S') or (i<R-1 and a[i+1][j]=='S') or (j>0 and a[i][j-1]=='S') or (j<C-1 and a[i][j+1]=='S') ):
                flag=-1
                return flag
    return flag

flag=sheep(a,R,C)

if flag==0:
    for i in range(R):
        for j in range(C):
            if a[i][j]=='.':
                a[i][j]='D'

if flag==-1:
    print('No')
else:
    print('Yes')
    for i in range(R):
        print(''.join(a[i]))
