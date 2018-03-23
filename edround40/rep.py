n=int(input())
s=list(input())

def rep(n,s):
    if len(set(s)) == n:
        return(n)
    else:
        for i in range(n//2,0,-1):
            # for j in range(n-i-i+1):
            # print(i)
            if s[:i] == s[i:i+i]:
                # print(s[j:j+i])
                # print(i)
                return n-i+1
        return n
print(rep(n,s))




# # Length of longest non-repeating substring can be recursively
# # defined as below.
# #
# # LCSRe(i, j) stores length of the matching and
# #             non-overlapping substrings ending
# #             with i'th and j'th characters.
# #
# # If str[i-1] == str[j-1] && (j-i) > LCSRe(i-1, j-1)
# #      LCSRe(i, j) = LCSRe(i-1, j-1) + 1,
# # Else
# #      LCSRe(i, j) = 0
# #
# # Where i varies from 1 to n and
# #       j varies from i+1 to n
#
# if len(set(s))==n:
#     print(n)
# else:
#     lcsr = [[0 for i in range(n)] for j in range(n)]
#     # print(lcsr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if s[i-1]==s[j-1] and (j-i) > lcsr[i-1][j-1]:
#                 lcsr[i][j] = lcsr[i-1][j-1]+1
#
#     max_val=0
#     for i in range(n):
#         max_val=max(max(lcsr[i]), max_val)
#         # print(max_val)
#     if max_val==1:
#         print(n-max_val)
#     else:
#         print(n-max_val+1)
