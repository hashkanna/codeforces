s=input()
from collections import Counter

def adorable(s):
    if len(set(s))==1:
        return 'No'
    if len(s)<4:
        return 'No'
    if len(set(s)) > 4:
        return 'No'
    if len(set(s))==2:
        d=Counter(s)
        for i in d:
            if d[i]==1:
                return 'No'
    return 'Yes'
print(adorable(s))
