from itertools import permutations

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [i, x.index(v)]

def check_valid(D,L,U,R,s,a,n,m):
    start_pos=index_2d(a,'S')
    end_pos=index_2d(a,'E')
    curr_pos=start_pos
    for i in s:
        if i==D:
            curr_pos[0]+=1
            if curr_pos[0] >= n or a[curr_pos[0]][curr_pos[1]] == '#':
                return 0
        if i==L:
            curr_pos[1]-=1
            if curr_pos[1] < 0 or a[curr_pos[0]][curr_pos[1]] == '#':
                return 0
        if i==U:
            curr_pos[0]-=1
            if curr_pos[0] < 0 or a[curr_pos[0]][curr_pos[1]] == '#':
                return 0
        if i==R:
            curr_pos[1]+=1
            if curr_pos[1] >= m or a[curr_pos[0]][curr_pos[1]] == '#':
                return 0
        if curr_pos == end_pos:
            return 1
    return 0

def robo(a,s,n,m):
    l=list(permutations(range(4)))
    c=0
    for i in l:
        D,L,U,R=i
        c+=check_valid(D,L,U,R,s,a,n,m)
    return c

n,m=list(map(int, input().split()))
a=[]
for i in range(n):
    a.append(list(input()))
s=list(map(int,input()))
print(robo(a,s,n,m))
