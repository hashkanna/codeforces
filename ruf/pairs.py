class DancingClass:
    def ncr(self, n, r):
        import operator as op
        from functools import reduce
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer//denom

    def checkOdds(self,n,k):
        import math
        count_vals=int(2**n)
        count=0
        for i in range(1,1+int(math.ceil(n/2.0))):
            # s=bin(i)[2:]
            j=n-i
            tmp=int(math.ceil(1.0*k/i))
            # print(tmp)
            if (j-tmp+1)>=1:
                count+=self.ncr(n,j)
        #print(count)

        if 2*count==count_vals:
            return 'Equal'
        elif 2*count>count_vals:
            return 'High'
        else:
            return 'Low'


d=DancingClass()
#print(d.checkOdds(3,2))
assert(d.checkOdds(2,1)=='Equal')
assert(d.checkOdds(3,2)=='High')
assert(d.checkOdds(4,4)=='Low')
assert(d.checkOdds(500,500)=='High')
assert(d.checkOdds(40,397)=='Low')
assert(d.checkOdds(1,1)=='Low')
