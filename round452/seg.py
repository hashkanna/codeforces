import heapq

def seg(n,a):
    heap=[]
    tup=[1,0,a[0]]
    for i in range(1,n):
        if a[i]==a[i-1]:
            tup=[1+tup[0],tup[1]]
        else:
            heapq.heappush(heap=heap,item=tup)
            t.append(tup)
            tup=[1,a[i]]



n=8
a=[13, 13, 7, 7, 7, 2, 2, 2]
