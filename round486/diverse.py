n,k=list(map(int, input().split(' ')))
a=list(map(int, input().split(' ')))

s = set([])
res = []
for ind, num in enumerate(a):
    if num not in s:
        s.add(num)
        res.append(ind+1)
    if len(res) == k:
        break
if len(res)==k:
    print('YES')
    print(*res)
else:
    print('NO')
