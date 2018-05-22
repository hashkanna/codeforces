from collections import defaultdict

d=defaultdict(list)
n,m=list(map(int,input().split(' ')))

# lst=[]
# for i in range(n):
#     lst.append(input())

flag=0
res=[]
c=0
for i in range(n):
    s=input()
    for j in range(m):
        if s[j]=='1' and j not in res:
            res.append(j)
            c+=1
            if c==m and i<(n-1):
                flag=1
                break

if flag==1:
    print('YES')
else:
    print('NO')


# lst=[]
# s=[]
# for i in range(m):
#     s.append(0)
#
# for i in range(n):
#     val=list(map(int,list(input())))
#     lst.append(val)
#     for j in range(m):
#         s[j]=min(2,s[j]+val[j])
# # print(s)
#
#
# def binadd(lst,s):
#     for i in lst:
#         res=[]
#         for x,y in zip(s,i):
#             res.append(x-y)
#         if 0 not in res:
#             return 'YES'
#     return 'NO'
#
# print(binadd(lst,s))
#
#
#
#
# # lst=[]
# # for i in range(n):
# #     lst.append(input())
# #
# # def add_fn(a,b):
# #     return bin(int(a,2) | int(b,2))[2:]
# #
# # def binadd(n,m,lst):
# #     for i in range(n):
# #         new_lst=lst[:i]+lst[i+1:]
# #         s=new_lst[0]
# #         for j in new_lst[1:]:
# #             s=add_fn(s,j)
# #         # print(s, len(s[2:]))
# #         if '0' not in s and len(s)==m:
# #             return 'YES'
# #     return 'NO'
# #
# # print(binadd(n,m,lst))
