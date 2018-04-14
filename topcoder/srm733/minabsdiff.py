class MinimizeAbsoluteDifferenceDiv2():
    def fn(self,list1):
        a,b,c=list1
        return abs((a/b)-c)

    def findTriple(self,x0,x1,x2):
        from itertools import permutations
        res_ind=0
        res_list=[(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        l=[x0,x1,x2]
        min_val=self.fn(l)
        p=list(permutations(l,3))
        for ind,x in enumerate(p):
            val=self.fn(x)
            # print(x,val)
            if val<=min_val:
                min_val=val
                # print(res_ind)
                res_ind=ind
        res_value = res_list[res_ind]
        #result=*res_value
        #result = str(res_value[0]) + ' ' + str(res_value[1]) + ' ' + str(res_value[2])
        return (res_value)

obj=MinimizeAbsoluteDifferenceDiv2()
print(obj.findTriple(1,1,1))
print(obj.findTriple(1,2,3))
print(obj.findTriple(7,20,5))
print(obj.findTriple(6,2,3))
print(obj.findTriple(10,11,111))
# print('{' + str(res_value[0]) + ', ' + str(res_value[1]) + ', ' + str(res_value[2]) + ' }')

# Problem Statement
#
# You are given three positive integers: the integers x0, x1, and x2. You have the following expression: |(?/?) - ?|. You want to replace the three question marks with your three integers in some order. In what order should you place the three integers if your goal is to make the result as small as possible?
# More formally, you have an expression of the form | (xa / xb) - xc |. Here, "/" denotes real division (e.g., 7/2 = 3.5), and "||" denotes absolute value. Your task is to choose three distinct subscripts a, b, c so that the value of the expression is as small as possible.
# Return a tuple (integer) with three elements: the optimal values {a, b, c}. If there are multiple optimal answers, you may return any of them.
# Definition
#
# Class:
# MinimizeAbsoluteDifferenceDiv2
# Method:
# findTriple
# Parameters:
# integer, integer, integer
# Returns:
# tuple (integer)
# Method signature:
# def findTriple(self, x0, x1, x2):
#
# Limits
#
# Time limit (s):
# 2.000
# Memory limit (MB):
# 256
# Constraints
# -
# x0 will be between 1 and 10,000, inclusive.
# -
# x1 will be between 1 and 10,000, inclusive.
# -
# x2 will be between 1 and 10,000, inclusive.
# Examples
# 0)
#
#
# 1
# 1
# 1
# Returns: {0, 1, 2 }
# Regardless of our choice of subscripts, the expression is always evaluated to |(1/1) - 1| = 0. Any of the six permutations of {0, 1, 2} is a correct answer.
# 1)
#
#
# 1
# 2
# 3
# Returns: {1, 2, 0 }
# The return value {1, 2, 0} corresponds to the expression |(x1 / x2) - x0| = |2/3 - 1| = 1/3 = 0.333333. This is the only optimal choice of {a, b, c}, all other choices produce expressions with a larger value.
# 2)
#
#
# 7
# 20
# 5
# Returns: {1, 0, 2 }
# This set of subscripts produces an expression with the value 15/7.
# 3)
#
#
# 6
# 2
# 3
# Returns: {0, 1, 2 }
# There are two correct answers: {0, 1, 2} and {0, 2, 1}. You may return either of them.
# 4)
#
#
# 10
# 11
# 111
# Returns: {2, 1, 0 }
