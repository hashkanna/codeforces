s=list(input())

tmp=''
res=''
if ('0' not in s) or ('2' not in s):
    res=''.join(sorted(s))
else:
    ind=s.index('2')
    res+=''.join(sorted(s[:ind]))
    ones=s[ind:].count('1')
    res+=ones*'1'
    # res+=2
    lst=[x for x in s[ind:] if x != '1']
    res+=''.join(lst)

print(res)
