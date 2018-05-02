n=int(input())
a=input()
zeros=a.count('0')
if '1' in a:
    res='1'+('0'*zeros)
else:
    res='0'
print(res)
