f0='What are you doing at the end of the world? Are you busy? Will you save us?'
f1='What are you doing while sending "' + f0 + '"? Are you busy? Will you send "' + f0 + '"?'
f2='What are you doing while sending "' + f1 + '"? Are you busy? Will you send "' + f1 + '"?'
print(len(f0))
print(len(f1))
print(len(f2))
from collections import defaultdict
d=defaultdict(list)
for i,j in enumerate(f0):
    d[j].append(i+1)

for i in d:
    print(i,d[i])
print(len(d))
d=defaultdict(list)
for i,j in enumerate(f1):
    d[j].append(i+1)
print('-----')
for i in d:
    print(i,d[i])
print(len(d))
d=defaultdict(list)
for i,j in enumerate(f2):
    d[j].append(i+1)
print('-----')
for i in d:
    print(i,d[i])
print(len(d))
