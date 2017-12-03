from collections import Counter
from fractions import Fraction
from math import factorial
from random import randint
import math
from collections import defaultdict

def vlad(n,a):
    # l=list(a)
    # s=set(l)
    # s_count=len(s)
    # print(s, s_count)
    d=defaultdict(int)
    for i,j in enumerate(a):
        d[j]=i
        # print(i)
        # if i in s:
        #     s.remove(i)
        #     s_count-=1
        #     if s_count == 0:
        #         return i
    return min(d,key=d.get)

n=int(input())
a=map(int, input().split())
# # n=200000
# a = [randint(1,10000) for _ in range(200000)]
print(vlad(n,a))
assert(vlad(5,[1,3,2,1,2]) == 3)
assert(vlad(6,[2,1,2,2,4,1]) == 2)
