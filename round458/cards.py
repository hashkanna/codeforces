n=int(input())
a=list(map(int, input().split()))
b=a.count(max(a))
if b%2!=0:
    print('Conan')
else:
    while b%2==0:
        m=max(a)
        a=[x for x in a if x!=m]
        if a==[]:
            print('Agasa')
            break
        b=a.count(max(a))
    if a!= []:
        if b%2!=0:
            print('Conan')
        else:
            print('Agasa')
