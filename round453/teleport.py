n,m=list(map(int, input().split()))
# ai=[]
# max=0
# prev_a, prev_b=list(map(int, input().split()))
# for i in range(n-1):
#     a,b=list(map(int, input().split()))
#     if b>=a and b>max and a<=prev_b:
#         max=b
#     if max==m:
#         print("YES")
# if max!=m:
#     print("NO")

s=[]
for i in range(n):
    a,b=list(map(int, input().split()))
    s+=list(range(a,b))
    if b==m:
        s.append(b)
    s=list(set(s))
# if b not in s:
#     s.append(b)
s=[x for x in s if x<=m]
# print(s)
if len(s)==m+1 and min(s)==0 and max(s)==m:
    print("YES")
else:
    print("NO")
