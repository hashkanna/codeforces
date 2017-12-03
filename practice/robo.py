import math
a,b=list(map(int, input().split()))
c,d=list(map(int, input().split()))
print(math.ceil((abs(c-a) + abs(d-b))/2))
