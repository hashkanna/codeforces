def subset_sum(integers, target_sum=0):
    """
    Returns a boolean indicating whether the given list of integers contains a
    (non-empty) subset that sums to the given value
    Parameters
    ----------
    integers: list of int
        The list of integers to consider
    target_sum: int
        The goal sum
    Returns
    ----------
    True if a non-empty subset that sums to target_sum exist, and
    False otherwise.
    """

    # We start by figuring out what the smallest and largest possible subset
    # sums are.
    positive = [integer for integer in integers if integer > 0]
    negative = [integer for integer in integers if integer < 0]
    # we'll refer to the elements of non_zeros as x_1 ... x_N
    # where N = len(non_zeros)
    non_zeros = positive + negative

    pos_sum = sum(positive)
    neg_sum = sum(negative)

    lookup_table = {}
    def _subset_sum_dp(index, goal_sum):
        # If the goal_sum is less than the sum of all negative integers in
        # the set, or greater than the sum of all positive integers, there's
        # no possible subset that sums to it
        if goal_sum < neg_sum or goal_sum > pos_sum:
            return False

        # In the base case our set of candidate integers only contains x_1,
        # so check if x_1 == goal_sum
        if index == 0:
            return non_zeros[0] == goal_sum

        # Check if we've called _subset_sum_dp with the same value of
        # index and goal_sum. If we have, return the memorized value instead
        # of evaluating the recursion again.
        key = (index, goal_sum)
        if key in lookup_table:
            return lookup_table[key]

        # Our recursion uses the following observation. If there exists a subset
        # summing to goal_sum and containing only the integers leading up to
        # and including the index (x_index), one of three following must hold:
        # 1. x_index == goal_sum, in which case x_index itself is a valid subset
        # 2. there's a solution to the subset sum problem using only
        #    x_1 ... x_{index-1}, in which case we can simply omit x_index.
        # 3. there's a solution to the subset sum problem with a target sum of
        #    the goal_sum - x_index and using only integers in the
        #    set x_1 ... x_{index-1}. In such cases, adding x_index to that
        #    problem's solution results in a solution to the current
        #    problem.

        result = non_zeros[index] == goal_sum or \
                 _subset_sum_dp(index-1, goal_sum) or \
                 _subset_sum_dp(index-1, goal_sum-non_zeros[index])

        # Memorize and return the result
        lookup_table[key] = result
        return result

    return _subset_sum_dp(len(non_zeros)-1, target_sum)

def main():
    """
    A simple test demonstrating the application of the subset_sum function
    to a list of integers.
    """
    n=int(input())
    l=list(range(1,n+1))
    target_sum = sum(l)//2
    result = subset_sum(l, target_sum=target_sum)
    print('The set %s %s a subset sum of %d.' % \
          (str(l), 'has' if result else 'does not have', target_sum))

if __name__ == '__main__':
    main()




# def isSubsetSum(set,n, sum) :
#
#     # Base Cases
#     if (sum == 0) :
#         return True
#     if (n == 0 and sum != 0) :
#         return False
#
#     # If last element is greater than
#     # sum, then ignore it
#     if (set[n - 1] > sum) :
#         return isSubsetSum(set, n - 1, sum);
#
#     # else, check if sum can be obtained
#     # by any of the following
#     # (a) including the last element
#     # (b) excluding the last element
#     return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])
#
#
#
# # def subsetsum(array,num):
# #
# #     if num == 0 or num < 1:
# #         return None
# #     elif len(array) == 0:
# #         return None
# #     else:
# #         if array[0] == num:
# #             return [array[0]]
# #         else:
# #             with_v = subsetsum(array[1:],(num - array[0]))
# #             if with_v:
# #                 return [array[0]] + with_v
# #             else:
# #                 return subsetsum(array[1:],num)
#
# # if sum(l)%2==0:
# #     print(0)
# # else:
# #     print(1)
# # a = subsetsum(l,sum(l)//2)
# # print(len(a), *a)
#
# # print(isSubsetSum(l,n,sum(l)//2))
#
# class Solution(object):
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         s = sum(nums)
#         if s % 2:
#             return False
#
#         dp = [False] * (s/2 + 1)
#         dp[0] = True
#         for num in nums:
#             for i in xrange(1, len(dp)):
#                 if num <= i:
#                     dp[i] = dp[i] or dp[i - num]
#         return dp[-1]
#
# a=Solution()
# print(a.canPartition)
