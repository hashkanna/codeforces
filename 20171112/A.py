from collections import Counter
from fractions import Fraction
from math import factorial
from itertools import permutations

# n=int(input)
def acm(a):
    for i in permutations(list(range(len(a))),3):
        if sum(a[x] for x in i)==sum(a[x] for x in [0,1,2,3,4,5] if x not in i):
            return "YES"
    return "NO"

a=list(map(int, input().split()))
print(acm(a))
