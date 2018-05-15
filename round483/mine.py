def count_bomb(a,list1):
    if a[list1[0]][list1[1]]=='*':
        return 1
    return 0

def check_valid(a,n,m):
    # res=0
    for i in range(n):
        for j in range(m):
            count=0
            left = []
            right = []
            top = []
            bottom = []
            topleft = []
            bottomright = []
            bottomleft = []
            topright = []

            if j-1>=0: left=[i,j-1]
            if j+1<m: right=[i,j+1]
            if i-1>=0: top=[i-1,j]
            if i+1<n: bottom=[i+1,j]
            if i-1>=0 and j-1>=0: topleft=[i-1,j-1]
            if i+1<n and j+1<m: bottomright=[i+1,j+1]
            if i+1<n and j-1>=0: bottomleft=[i+1,j-1]
            if i-1>=0 and j+1<m: topright=[i-1,j+1]
            for x in [left, right, top, bottom, topleft, bottomright, bottomleft, topright]:
                if x!=[]:

                    count += count_bomb(a,x)
                    #print('kanna ',x, i, j, right, count_bomb(a,x), count)
            # print('count', a, i, j, count)
            if a[i][j]=='.' and count!=0:
                # print(i,j)
                #print('kanna ',x, i, j, right, count_bomb(a,x), count)
                return False

            if a[i][j]!='.' and a[i][j]!='*' and int(a[i][j])!=count:
                # print(i,j)
                # print(left, right, top, bottom, topleft, bottomright, bottomleft, topright, [i-1,j+1])
                # print('kanna ',x, i, j, right, count)
                return False
    return True

n,m=list(map(int, input().split(' ')))
a=[]
for i in range(n):
    a.append(input())
# print(a)
if check_valid(a,n,m):
    print('YES')
else:
    print('NO')
