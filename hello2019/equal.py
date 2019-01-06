import itertools

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# numbers = [1, 2, 3, 7, 7, 9, 10]
# result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq)%360 == 0]
# print(result)

flag=-1
for i in set(itertools.permutations([1]*n+[-1]*n,n)):
    sum_val=0
    for j in range(n):
        sum_val+=numbers[j]*i[j]
    if sum_val%360 == 0:
        print("YES")
        flag=0
        break
if flag==-1:
    print("NO")
# def findSplitPoint(arr, n) :
#
#     leftSum = 0
#
#     # traverse array element
#     for i in range(0, n) :
#
#         # add current element to left Sum
#         leftSum += arr[i]
#
#         # find sum of rest array elements (rightSum)
#         rightSum = 0
#         for j in range(i+1, n) :
#             rightSum += arr[j]
#
#         # split poindex
#         if (leftSum == rightSum) :
#             return i+1
#
#
#     # if it is not possible to split array into
#     # two parts
#     return -1
#
#
# # Prints two parts after finding split pousing
# # findSplitPoint()
# def printTwoParts(arr, n) :
#
#     splitPo = findSplitPoint(arr, n)
#
#     if (splitPo == -1 or splitPo == n ) :
#         #print ("Not Possible")
#         return -1
#     return 0
#     # for i in range(0, n) :
#     #     if(splitPo == i) :
#     #         print ("")
#     #     print (str(arr[i]) + ' ',end='')
#
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# #arr = [1 , 2 , 3 , 4 , 5 , 5]
# #n = len(arr)
# if sum(arr)%360 == 0:
#     print("YES")
# elif printTwoParts(arr, n) == -1:
#     print("NO")
# else:
#     print("YES")
