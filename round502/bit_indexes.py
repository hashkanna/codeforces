n=int(input())
a=input()
b=input()

b_0_indexes = [i for i,x in enumerate(b) if x=='0']
a_0_indexes = [i for i,x in enumerate(a) if x=='0' and i not in b_0_indexes]
a_1_indexes = [i for i,x in enumerate(a) if x=='1']

# print(b_0_indexes)
# print(a_0_indexes)
# print(a_1_indexes)

ans=0
a_count=0
b_count=0
for i in b_0_indexes:
    if a[i]=='0':
        a_count+=1
    else:
        b_count+=1

ans=(a_count*len(a_1_indexes)) + (b_count*len(a_0_indexes))
print(ans)
