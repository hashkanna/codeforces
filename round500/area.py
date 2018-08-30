n=int(input())
a=list(map(int, input().split(' ')))

# import heapq
# max_elems = heapq.nlargest(4,a)
# min_elems = heapq.nsmallest(4,a)
# print(min_elems, max_elems)

def val(p1,p2):
    return (p2[0]-p1[0])*(p2[1]-p1[1])

if n==1:
    print(0)
else:
    a=sorted(a)
    p1=[a[0],a[-n]]
    p2=[a[n-1],a[-1]]
    res=val(p1,p2)

    # new_p1=[a[-n],a[0]]
    # new_p2=[a[-1],a[n-1]]
    # res=min(res, val(new_p1, new_p2))
    print(p1)
    print(p2)
    print(res)
