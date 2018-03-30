# https://www.quora.com/How-do-i-solve-prefix-palindrome-problem-using-Z-algorithm-in-O-n-time

def z_advanced(s):
    """An advanced computation of Z-values of a string."""

    Z = [0] * len(s)
    Z[0] = len(s)

    rt = 0
    lt = 0

    for k in range(1, len(s)):
        if k > rt:
            # If k is outside the current Z-box, do naive computation.
            n = 0
            while n + k < len(s) and s[n] == s[n+k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k+n-1
        else:
            # If k is inside the current Z-box, consider two cases.

            p = k - lt  # Pair index.
            right_part_len = rt - k + 1

            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k

                lt = k
                rt = i - 1
    return Z

s=input()
n=len(s)
# after reversing S1="ababa"
# now S2=S+S1;
s+=s[::-1]
z=z_advanced(s)
z[0]=0
# print(z)
# zz=z[n:] #we'll ignore the values of indexes < S.size
# pal=[0]*n
# for i in range(len(zz)):
#     if len(z)-i==z[i]:
#         pal[z[i]]=1

print(max(z[n:]))

# i - S.size() + k = S.size() then pal[z[i]] is a palindrome.
#
# print(*z)
