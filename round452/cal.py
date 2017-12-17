from collections import Counter
from collections import defaultdict
n=int(input())
l=input().split()
d=Counter(l)
indices=defaultdict(list)
for i in range(n):
    indices[l[i]].append(i)

# for i in ['28', '29', '30', '31']:
#     if i not in d:
#         d[i]

if d['29']>1:
    print('No')
elif d['28']>2:
    print('No')
elif d[28]==2:
    if indices['28'][1]-indices['28'][0] != 12:
        print('No')
elif d[28]==1 and d[29]==1:
    if abs(indices['28'][1]-indices['28'][0]) != 12:
        print('No')
else:
    for i in range(n):
        if a[i+1] and a[i+2]
# elif
# indices['28']!=[]:
#     if
#      - indices[29]:
#
# print(indices)
