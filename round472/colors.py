n=int(input())
s=list(input())

# from collections import defaultdict
# d=defaultdict(list)
# for ind,i in enumerate(s):
#     d[i].append(int)

# count=1
# for i in d['?']:

def colors(n,s):
    count=1
    for i in range(n-1):
        if s[i]==s[i+1] and s[i]!='?':
            return 'No'
    for i in range(n):
        if s[i]=='?':
            if i==0:
                count=2
                return 'Yes'
            if i==n-1:
                count=2
                return 'Yes'
            if s[i-1]==s[i+1]:
                count=2
                return 'Yes'
            if s[i+1]=='?':
                return 'Yes'
    return 'No'

print(colors(n,s))
