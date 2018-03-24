a=[1]
for i in range(3,31):
    num=2
    while(num**i<1+10**18):
        a.append(num**i)
        num+=1
        # print(a)
b=sorted(a)
import math
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

c=[x for x in b if not is_square(x)]


import math
def CountSquares(a,b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

def findClosest(arr, n, target):

    # Corner cases
    if (target <= arr[0]):
        return 0
    if (target >= arr[n - 1]):
        return n - 1

    # Doing binary search
    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) // 2

        if (arr[mid] == target):
            return mid

        # If target is less than array
        # element, then search in left
        if (target < arr[mid]) :

            # If target is greater than previous
            # to mid, return closest of two
            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr,mid - 1, mid, target)

            # Repeat for left half
            j = mid

        # If target is greater than mid
        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr,mid, mid + 1, target)

            # update i
            i = mid + 1

    # Only single element left after search
    return mid


# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def getClosest(arr,val1, val2, target):
    if (target - arr[val1] >= arr[val2] - target):
        return val2
    else:
        return val1

nn=int(input())
for i in range(nn):
    a,b=list(map(int,input().split(' ')))
    count = CountSquares(a,b)
    # Driver code
    n = len(c)
    a1=findClosest(c, n, a)
    a2=findClosest(c, n, b)
    # print(a1,a2)
    count+=a2-a1+1
    if a>c[a1]:
        count-=1
    if b<c[a2]:
        count+=1
    if is_square(a):
        count-=1
    if is_square(b):
        count-=1
    if is_square(a) and is_square(b) and a==b:
        count+=2
    if a<c[0]:
        count-=1
    if b<c[0]:
        count-=1
    # if a not in c and b not in c:
    #     count-=1
    # print(findClosest(arr, n, target))
    print(count)
