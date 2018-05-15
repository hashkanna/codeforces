n,k=list(map(int, input().split(' ')))
def print_res(lst):
    for i in lst:
        print(''.join(i))
res=[['.']*n] + [['.']*n] + [['.']*n] + [['.']*n]


if k==0:
    print('YES')
    print_res(res)
elif k>(n-2)*2:
    print('NO')
elif k==n-2:
    print('YES')
    res[1]=['.']+['#'*k]+['.']
    # res[1][0]='.'
    # res[1][-1]='.'
    print_res(res)
elif k%2==0:
    print("YES")
    for i in range(k//2):
        res[1][i+1]='#'
        res[2][i+1]='#'
    print_res(res)
elif k<(n-2):
    print("YES")
    res[1]=['.'*((n-k)//2)]+['#'*(k)]+['.'*((n-k)//2)]
    print_res(res)
elif k>(n-2):
     print("YES")
     res[1]=['.']+['#'*(n-2)]+['.']
     x=(k-n+2)//2
     for i in range(x):
         res[2][i+1]='#'
         res[2][-i-2]='#'
     # res[2]=['.']+['#'*()]+['.']+['#'*((k-n+2)//2)]+['.']
     print_res(res)
else:
    print('NO')
