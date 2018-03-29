def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def collinear(A,B,C):
    return (B[1] - C[1]) * (C[0] - B[0]) - (B[0] - A[0]) * (C[1] - B[1]) == 0

def point_on_segment(a,b,c):
    res=((b[0] - a[0]) * (c[1]- a[1])) - ((c[0] - a[0]) * (b[1] - a[1]))
    # print(res)
    if res==0:
        if a[0]!=b[0]:
            if a[0] <= c[0] <= b[0] or b[0] <= c[0] <= a[0]:
                return True
            else:
                return False
        else:
            if a[1] <= c[1] <= b[1] or b[1] <= c[1] <= a[1]:
                return True
            else:
                return False
    else:
        return False

n=int(input())
points=[]
for i in range(n):
    l=list(map(int,input().split(' ')))
    # ll=[]
    # ll.append(l[2]-l[0])
    # ll.append(l[3]-l[1])
    points.append(l)
# print(points)

#             AA=points[i][:2]
#             BB=points[i][2:4]
#             CC=points[j][:2]
#             DD=points[j][2:4]

c=0
for i in range(n-1):
    for j in range(i+1,n):
        AA=points[i][:2]
        BB=points[i][2:4]
        CC=points[j][:2]
        DD=points[j][2:4]

        if point_on_segment(AA,BB,CC):
            c+=1
        elif point_on_segment(AA,BB,DD):
            c+=1
        elif point_on_segment(CC,DD,AA):
            c+=1
        elif point_on_segment(CC,DD,BB):
            c+=1
print(c)
#         print(intersect(points[i][:2], points[i][2:4], points[j][:2], points[j][2:4]))
#         if intersect(points[i][:2], points[i][2:4], points[j][:2], points[j][2:4]):
#             c+=1
#         if not intersect(points[i][:2], points[i][2:4], points[j][:2], points[j][2:4]):
#             AA=points[i][:2]
#             BB=points[i][2:4]
#             CC=points[j][:2]
#             DD=points[j][2:4]
#             if collinear(AA,BB,CC):
#                 c+=1
#             elif collinear(AA,BB,DD) and ccw(AA,BB,DD):
#                 c+=1
#             elif collinear(AA,CC,DD) and ccw(AA,CC,DD):
#                 c+=1
#             elif collinear(BB,CC,DD) and ccw(BB,CC,DD):
#                 c+=1
#
#             # or collinear(AA,CC,DD) or collinear(AA,BB,DD) or collinear(BB,CC,DD)):
#
# print(c)
