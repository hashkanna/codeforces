def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

n=int(input())
p=[]
for i in range(n):
    p.append(list(map(int, input().split(' '))))
# print(p)
print(area(p))
