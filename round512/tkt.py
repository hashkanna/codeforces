def rec(a,s,sum_val,res):
    b=a[:]
    for j in range(len(a)):
        if sum_val+b[j]==res:
            del(a[j])
            return 1
        elif sum_val+b[j]<res:
            s.append(b[j])
            sum_val+=a[j]
            del(a[j])
        else:
            if len(s)==1:
                return -1
    return 0

def calc():
    n=int(input())
    a=sorted(list(map(int, input())), reverse=True)
    ss=sum(a)
    if ss%2!=0:
        return -1
    elif a[0]>ss//2:
        return -1
    else:
        for i in range(a[0],(ss//2)+1):
            if ss%i == 0:
                res=i
        for i in range(ss//res):
            s=[]
            sum_val=0
            ans=rec(a,s,sum_val,res)
            if ans==-1:
                return -1
            elif ans==1:
                s=[]
                sum_val=0
                if a==[]:
                    return "YES"
                rec(a,s,sum_val,res)
            else:
                a.append(s[-1])
                del(s[-1])
                rec(a,s,sum(s),res)
print(calc())
