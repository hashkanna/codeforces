from itertools import combinations_with_replacement
l=['(',')','[',']']

def is_valid(ll):
    stack=[]
    for i in ll:
        if i=='[' or i=='(':
            stack.append(i)
        elif i==']':
            if stack==[] or stack[-1]!='[':
                return False
            else:
                stack.pop()
        elif i==')':
            if stack==[] or stack[-1]!='(':
                return False
            else:
                stack.pop()
    return stack==[]

n=int(input())
if (n%2!=0):
    print()
else:
    l*=(n//2)
    res=[]
    for i in combinations_with_replacement(l,n):
        # print(i, is_valid(i))
        if is_valid(i):
            if ''.join(i) not in res:
                print(''.join(i))
                res.append(''.join(i))
