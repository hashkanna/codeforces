s=[0]
for i in range(1,1000):
    s.append(i*i)

n=int(input())
a=list(map(int,input().split()))
a=sorted(a, reverse=True)
for j in a:
    if j not in s:
        print(j)
        break
