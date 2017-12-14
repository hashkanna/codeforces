# class Solution(object):
#     def findLengthOfLCIS(self, nums):
#         ans = anchor = 0
#         for i in range(len(nums)):
#             if i and nums[i-1] >= nums[i]: anchor = i
#             ans = max(ans, i - anchor + 1)
#         return ans

# class Solution(object):
#     def findLengthOfLCIS(self, nums):
#         answers = []
#         anchors = []
#         anchor=0
#         ans=0
#         for i in range(len(nums)):
#             if i and nums[i-1] >= nums[i]:
#                 anchor=i
#                 anchors.append(i-1)
#             # ans = max(ans, i - anchor + 1)
#             # ans = i - anchor + 1
#             # answers.append(ans)
#         # anchors.append(i)
#         print(anchors)
#         for i in range(1, len(anchors)):
#             if anchors[i]
#         return anchors


class Solution(object):
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(2, len(nums)):
            if nums[i-2] >= nums[i]:
                anchor = i
                print(anchor)
            if i - anchor + 1 > ans:
                ans = max(ans, i - anchor + 1)
                ind = i
        return ans, ind


# n=int(input())
# l=list(map(int, input().split()))
s=Solution()
c=0
n=100000
from random import randint
# l=[randint(1,100000) for i in range(100000)]
l=[9,8,9,6,5,4,5,6,8,2,11,3,4]
# for i in range(n):
#     m=l[:i]+l[i+1:]
#     elem, cnt = l[i], s.findLengthOfLCIS(m)
#     if c<cnt:
#         c=cnt
#         e=elem
#     elif c==cnt:
#         e=min(elem, e)
#     print(e,c)
# print(e,c)
# print(e)
print(s.findLengthOfLCIS(l))
