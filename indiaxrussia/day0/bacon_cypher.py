s=input()
count=0
ss=[]
for i in range(1,len(s)+1):
    j=0
    while j+i<=len(s):
        ss.append(s[j:j+i])
        j+=1
print(len(set(ss)))

# def z_function(string1):
#     n = len(string1)
#     z = [0] * n
#
#     zbox_l, zbox_r, z[0] = 0, 0, n
#     for i in range(1, n):
#         if i < zbox_r:              # i is within a zbox
#             k = i - zbox_l
#             if z[k] < zbox_r - i:
#                 z[i] = z[k]         # Full optimization
#                 continue
#             zbox_l = i              # Partial optimization
#         else:
#             zbox_l = zbox_r = i     # Match from scratch
#         while zbox_r < n and string1[zbox_r - zbox_l] == string1[zbox_r]:
#             zbox_r += 1
#         z[i] = zbox_r - zbox_l
#     return z
#
# for i in range(len(s)):
#     x = s[:i+1]
#     x = x[::-1]
#     z = z_function(x)
#     print(x,z)
#     mx = 0
#     # foreach j to x.size()-1
#     for j in range(len(x)):
#         mx = max(mx,z[j])
#     count += (i+1) - mx
#
# print(count)

# _end = 'A'
# def make_trie(*words):
#      global count
#      count=0
#      root = dict()
#      for word in words:
#          current_dict = root
#          for letter in word:
#              if letter not in current_dict:
#                  count+=1
#              current_dict = current_dict.setdefault(letter, {})
#          current_dict[_end] = _end
#      return root
#
# # build suffixes
# suffixes=[]
# for i in range(len(s)):
#     suffixes.append(s[i:])
# # suffixes.append('A')
# # print(*suffixes)
#
# # print(make_trie(*suffixes))
#
# make_trie(*suffixes)
# print(count)
#
# # def count_nodes(t,count):
# #     for i in t:
# #         if type(t[i]) is dict:
# #             count.append(i)
# #             # count+=1
# #             count_nodes(t[i],count)
# #         # else:
# #         #     return count_nodes(t[i],count+1)
# #     return count
# #
# # print(len(count_nodes(suffix_tries,[])))
# # count_val=0
# # for i in suffix_tries:
# #     print(count_nodes(i, 0))
#
#
# # print(make_trie('aaba', 'aba', 'ba', 'a'))
