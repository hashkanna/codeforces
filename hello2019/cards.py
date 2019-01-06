a = input()
l = list(input().split(' '))

flag=-1
for i in l:
    if a[0]==i[0] or a[1]==i[1]:
        print("YES")
        flag=0
        break

if flag==-1:
    print("NO")
