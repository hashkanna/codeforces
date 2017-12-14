# from collections import Counter
# def count_box(a):
#     set_a = set(a)
#     if len(set_a) == 1:
#         return 1
#     a.sort()
#     return len(a)

from collections import Counter
n=int(input())
a=list(map(int, input().split()))
# count=0
# while a!=[]:
#     print(a)
#     count+=1
#     a = [i for i in a if a.count(i)>1]
print(max(Counter(a).items(), key=lambda x: x[1])[1])
