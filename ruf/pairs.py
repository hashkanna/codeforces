class DancingClass:
    def checkOdds(self,n,k):
        import math
        from functools import reduce
        count_vals=int(2**n)
        count=0
        for i in range(1,1+math.ceil(n/2)):
            # s=bin(i)[2:]
            j=n-i
            tmp=math.ceil(k//i)
            # print(tmp)
            if (j-tmp+1)>=1:
                mul=1
                for x in range(i,j):
                    mul*=x
                count+=2*mul
        print(count)

        if 2*count==count_vals:
            return 'Equal'
        elif 2*count>count_vals:
            return 'High'
        else:
            return 'Low'


d=DancingClass()
# print(d.checkOdds(500,500))
assert(d.checkOdds(2,1)=='Equal')
# assert(d.checkOdds(3,2)=='High')
assert(d.checkOdds(4,4)=='Low')
assert(d.checkOdds(500,500)=='High')
assert(d.checkOdds(40,397)=='Low')
assert(d.checkOdds(1,1)=='High')
