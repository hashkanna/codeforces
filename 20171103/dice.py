def dice(n,a):
    s=0
    if n==1:
        for i in range(1,10):
            if str(i) in a[0]:
                s+=1
            else:
                return s
    elif n==2:
        for i in range(1,10):
            if str(i) in a[0]+a[1]:
                s+=1
            else:
                return s

        for i in range(10,100):
            c=[]
            d=[]
            if str(i)[0] in a[0]:
                c.append(0)
            if str(i)[0] in a[1]:
                c.append(1)
            if str(i)[1] in a[0]:
                d.append(0)
            if str(i)[1] in a[1]:
                d.append(1)
            if sorted(set(list(set(c)) + list(set(d)))) == sorted(set(str(i))):
                s+=1
            else:
                return s
        return s

    elif n==3:
        for i in range(1,10):
            if str(i) in a[0]+a[1]+a[2]:
                s+=1
            else:
                return s

        for i in range(10,100):
            c=[]
            d=[]
            if str(i)[0] in a[0]:
                c.append(0)
            if str(i)[0] in a[1]:
                c.append(1)
            if str(i)[0] in a[2]:
                c.append(2)
            if str(i)[1] in a[0]:
                d.append(0)
            if str(i)[1] in a[1]:
                d.append(1)
            if str(i)[1] in a[2]:
                d.append(2)
            if sorted(set(list(set(c)) + list(set(d)))) == sorted(set(str(i))):
                s+=1
            else:
                return s
        return s

        for i in range(100,1000):
            c=[]
            d=[]
            e=[]
            if str(i)[0] in a[0]:
                c.append(0)
            if str(i)[0] in a[1]:
                c.append(1)
            if str(i)[0] in a[2]:
                c.append(2)
            if str(i)[1] in a[0]:
                d.append(0)
            if str(i)[1] in a[1]:
                d.append(1)
            if str(i)[1] in a[2]:
                d.append(2)
            if str(i)[2] in a[0]:
                e.append(0)
            if str(i)[2] in a[1]:
                e.append(1)
            if str(i)[2] in a[2]:
                e.append(2)

            if sorted(set(list(set(c)) + list(set(d)) + list(set(e)))) == sorted(set(str(i))):
                s+=1
            else:
                return s
        return s



n=int(input())
a=[list(input()) for _ in range(n)]
print(dice(n,a))
