n = int(input())
a = list(map(int,input().split()))
a = [x-1 for x in a]

result="NO"
for i in range(n):
    if (a[i] == a[a[a[a[i]]]]) and (a[i] != a[a[a[i]]]):
        result="YES"
        break
print(result)
