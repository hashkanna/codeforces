# class Solution:
#     # @param {string} s
#     # @return {integer}
#     def minCut(self, s):
#         if not s:
#             return 0
#
#         dp = [2147483647] * (len(s) + 1)
#         dp[0] = -1
#
#         for i in range(1, len(s) + 1):
#             for j in range(i):
#                 tmp = s[j:i]
#                 if tmp == tmp[::-1]:
#                     dp[i] = min(dp[i], dp[j] + 1)
#         return dp[-1]+1
#
# def main():
#     sol = Solution()
#     s = input()
#     print(sol.minCut(s))

from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def pal(s,i):
    set1 = set()

def pal_count(n,s):

    set1 = set()

    for c in s:
        if c in set1:
            set1.remove(c)
        else:
            set1.add(c)

    for f in sorted(factors(n)):
        if len(set1) <= f:
            a = []
            for i in range(f):
                
            return f

def main():
    n = int(input())
    s = input()
    print(pal_count(n,s))

if __name__ == '__main__':
    main()
