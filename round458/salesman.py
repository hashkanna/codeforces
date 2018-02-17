from collections import defaultdict
d=defaultdict(list)
d[0]=[1]
d[1]=[2,4,8,16,32,64,128,256,512]

for i in range(2,1001):
    if bin(i)[2:].count('1') in d[0]+d[1] and i not in d[0]+d[1]:
        d[2].append(i)

for i in range(2,1001):
    if bin(i)[2:].count('1') in d[0]+d[1]+d[2] and i not in d[0]+d[1]+d[2]:
        d[3].append(i)

for i in range(2,1001):
    if bin(i)[2:].count('1') in d[0]+d[1]+d[2]+d[3] and i not in d[0]+d[1]+d[2]+d[3]:
        d[4].append(i)
