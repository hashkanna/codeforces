n=int(input())
s=list(map(int, input().split(' ')))
c=list(map(int, input().split(' ')))

def minSum(s,c,n):
    ss=[i[0] for i in sorted(enumerate(s), key=lambda x:x[1])]
    # sort(s_arr, s_arr + n);

    # // Return the maximum of product of last three
    # // elements and product of first two elements
    # // and last element
    return ss, min(c[ss[0]] + c[ss[1]] + c[ss[2]],
               c[ss[n-1]] + c[ss[n-2]] + c[ss[n-3]]);
    # return indices


print(minSum(s,c,n))
# val=-1
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1,n):
#             if s[i]<s[j]<s[k]:
#                 # print(s[i],s[j],s[k],c[i]+c[j]+c[k])
#                 if val==-1:
#                     val=c[i]+c[j]+c[k]
#                 else:
#                     val=min(val, c[i]+c[j]+c[k])
#
# print(val)

# val = -1
# ss = s[:3]
# cc = c[:3]
#
# if ss[0]<ss[1]<ss[2]:
#     val=sum(cc[:3])
#
# for i in range(3,n):
#     if (s[i] < s[2]) and (s[i] > s[1]):
