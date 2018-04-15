def is_root(n,r):
    r_root = n**(1./r)
    return round(r_root) ** r == n

import math
def CountSquares(a,b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

a=[1]
# others=[1, 8, 16, 27, 32, 64, 81, 125, 128, 216, 243, 256, 343, 512, 625, 729, 1000, 1024, 1296, 1331, 1728, 2048, 2187, 2197, 2401, 2744, 3125, 3375, 4096, 4913, 5832, 6561, 6859, 7776, 8000, 8192, 9261, 10000, 10648, 12167, 13824, 14641, 15625, 16384, 16807, 17576, 19683, 20736, 21952, 24389, 27000, 28561, 29791, 32768, 35937, 38416, 39304, 42875, 46656, 50625, 50653, 54872, 59049, 59319, 64000, 65536, 68921, 74088, 78125, 79507, 83521, 85184, 91125, 97336, 100000, 103823, 104976, 110592, 117649, 125000, 130321, 131072, 132651, 140608, 148877, 157464, 160000, 161051, 166375, 175616, 177147, 185193, 194481, 195112, 205379, 216000, 226981, 234256, 238328, 248832, 250047, 262144, 274625, 279841, 279936, 287496, 300763, 314432, 328509, 331776, 343000, 357911, 371293, 373248, 389017, 390625, 405224, 421875, 438976, 456533, 456976, 474552, 493039, 512000, 524288, 531441, 537824, 551368, 571787, 592704, 614125, 614656, 636056, 658503, 681472, 704969, 707281, 729000, 753571, 759375, 778688, 804357, 810000, 823543, 830584, 857375, 884736, 912673, 923521, 941192, 970299]

# others=[x for x in others if round(x**(1/2))**2!=x]

for i in range(2,10**18):
    for j in range(3,61):
        if is_root(i,j):
            a.append(i)
            break
# print(a)
# print(others)
# print(len(others))
# print(CountSquares(4,10**18))

# a=[1]
# for i in range(3,31):
#     num=2
#     while(num**i<1+10**18):
#         a.append(num**i)
#         num+=1
#         # print(a)
# b=sorted(a)
# import math
# def is_square(integer):
#     root = math.sqrt(integer)
#     if int(root + 0.5) ** 2 == integer:
#         return True
#     else:
#         return False
#
# c=[x for x in b if not is_square(x)]
#
#
# import math
# def CountSquares(a,b):x
#     return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
#
# def findClosest(arr, n, target):
#
#     # Corner cases
#     if (target <= arr[0]):
#         return 0
#     if (target >= arr[n - 1]):
#         return n - 1
#
#     # Doing binary search
#     i = 0; j = n; mid = 0
#     while (i < j):
#         mid = (i + j) // 2
#
#         if (arr[mid] == target):
#             return mid
#
#         # If target is less than array
#         # element, then search in left
#         if (target < arr[mid]) :
#
#             # If target is greater than previous
#             # to mid, return closest of two
#             if (mid > 0 and target > arr[mid - 1]):
#                 return getClosest(arr,mid - 1, mid, target)
#
#             # Repeat for left half
#             j = mid
#
#         # If target is greater than mid
#         else :
#             if (mid < n - 1 and target < arr[mid + 1]):
#                 return getClosest(arr,mid, mid + 1, target)
#
#             # update i
#             i = mid + 1
#
#     # Only single element left after search
#     return mid
#
#
# # Method to compare which one is the more close.
# # We find the closest by taking the difference
# # between the target and both values. It assumes
# # that val2 is greater than val1 and target lies
# # between these two.
# def getClosest(arr,val1, val2, target):
#     if (target - arr[val1] >= arr[val2] - target):
#         return val2
#     else:
#         return val1
#
# nn=int(input())
# for i in range(nn):
#     a,b=list(map(int,input().split(' ')))
#     count = CountSquares(a,b)
#     # Driver code
#     n = len(c)
#     a1=findClosest(c, n, a)
#     a2=findClosest(c, n, b)
#     # print(a1,a2)
#     count+=a2-a1+1
#     if a>c[a1]:
#         count-=1
#     if b<c[a2]:
#         count+=1
#     if is_square(a):
#         count-=1
#     if is_square(b):
#         count-=1
#     if is_square(a) and is_square(b) and a==b:
#         count+=2
#     if a<c[0]:
#         count-=1
#     if b<c[0]:
#         count-=1
#     # if a not in c and b not in c:
#     #     count-=1
#     # print(findClosest(arr, n, target))
#     print(count)
