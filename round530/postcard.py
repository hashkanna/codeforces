import re

s = input()
k = int(input())

question_count=s.count('?')
star_count=s.count('*')
s_len=len(s)
min_chars = s_len - 2*(question_count+star_count)

#print(k,min_chars)

if k<min_chars:
    print('Impossible')
else:
    lis=[]
    i=0
    tmp_list=[]
    while i<s_len-1:
        if s[i+1]=='?' or s[i+1]=='*':
            if tmp_list!=[]: lis.append(tmp_list)
            lis.append(list(s[i:i+2]))
            tmp_list=[]
            i+=2
        else:
            tmp_list.append(s[i])
            i+=1
    if s[-1] not in ['*','?']: tmp_list.append(s[-1])
    if tmp_list: lis.append(tmp_list)
    #print(lis)

    diff=k-min_chars
    res=''
    for elem in lis:
        if diff!=0 and '?' in elem:
            diff-=1
            res+=elem[0]
        elif diff!=0 and '*' in elem:
            res+=elem[0]*diff
            diff=0
        if '?' not in elem and '*' not in elem:
            res+=''.join(elem)
    if len(res)==k:
        print(res)
    else:
        print('Impossible')
