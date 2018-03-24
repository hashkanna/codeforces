# # Python code to implement iterative Binary
# # Search.
#
# # It returns location of x in given array arr
# # if present, else returns -1
#
# import math
# def CountSquares(a,b):
#     return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
#
# import math
# def is_square(integer):
#     root = math.sqrt(integer)
#     if int(root + 0.5) ** 2 == integer:
#         return True
#     else:
#         return False
#

# Python3 program to find element
# closet to given target.

# Returns element closest to target in arr[]
def findClosest(arr, n, target):

    # Corner cases
    if (target <= arr[0]):
        return 0
    if (target >= arr[n - 1]):
        return n - 1

    # Doing binary search
    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) / 2

        if (arr[mid] == target):
            return mid

        # If target is less than array
        # element, then search in left
        if (target < arr[mid]) :

            # If target is greater than previous
            # to mid, return closest of two
            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)

            # Repeat for left half
            j = mid

        # If target is greater than mid
        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)

            # update i
            i = mid + 1

    # Only single element left after search
    return mid


# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def getClosest(val1, val2, target):
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val2

# Driver code
arr = [1, 2, 4, 5, 6, 6, 8, 9]
n = len(arr)
target = 11
print(findClosest(arr, n, target))
