from collections import defaultdict
d=defaultdict(list)
n=int(input())
for i in range(n):
    m=input().split()
    name=m[0]
    numbers=set(m[2:]+d[name])
    out=[]
    for num in numbers:
        for num1 in numbers:
            if num!=num1 and num1.endswith(num):
                out.append(num)
    numbers = list(set(numbers) - set(out))
    # print(name, numbers)
    d[name]=numbers

print(len(d))
for i in d:
    print(i, len(d[i]), ' '.join(d[i]))
