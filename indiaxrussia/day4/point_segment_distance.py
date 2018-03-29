import math
l=list(map(int, input().split(' ')))
c=l[:2]
a=l[2:4]
b=l[4:6]


def dot_product(a,b,c):
    ab=[b[0]-a[0],b[1]-a[1]]
    bc=[c[0]-b[0],c[1]-b[1]]
    # print(ab,bc)
    return ab[0]*bc[0] + ab[1]*bc[1]

def cross_product(a,b,c):
    ab=[b[0]-a[0],b[1]-a[1]]
    ac=[c[0]-a[0],c[1]-a[1]]
    return (ab[0]*ac[1]) - (ab[1] * ac[0])

def dist(a,b):
    d1 = a[0] - b[0]
    d2 = a[1] - b[1]
    return 0.000000000001 + math.sqrt(d1*d1+d2*d2)

res = cross_product(a,b,c) / dist(a,b)
dot1 = dot_product(a,b,c)
if (dot1 > 0):
    res=dist(b,c)
dot2 = dot_product(b,a,c)
if (dot2 > 0):
    res=dist(a,c)

print('%.5f' % abs(res))


# res = cross_product(a,b,c) / dist(a,b)

# print('%.5f'%res)


# //Compute the dot product AB ⋅ BC
#     int dot(int[] A, int[] B, int[] C){
#         AB = new int[2];
#         BC = new int[2];
#         AB[0] = B[0]-A[0];
#         AB[1] = B[1]-A[1];
#         BC[0] = C[0]-B[0];
#         BC[1] = C[1]-B[1];
#         int dot = AB[0] * BC[0] + AB[1] * BC[1];
#         return dot;
#     }
#     //Compute the cross product AB x AC
#     int cross(int[] A, int[] B, int[] C){
#         AB = new int[2];
#         AC = new int[2];
#         AB[0] = B[0]-A[0];
#         AB[1] = B[1]-A[1];
#         AC[0] = C[0]-A[0];
#         AC[1] = C[1]-A[1];
#         int cross = AB[0] * AC[1] - AB[1] * AC[0];
#         return cross;
#     }
#     //Compute the distance from A to B
#     double distance(int[] A, int[] B){
#         int d1 = A[0] - B[0];
#         int d2 = A[1] - B[1];
#         return sqrt(d1*d1+d2*d2);
#     }
#     //Compute the distance from AB to C
#     //if isSegment is true, AB is a segment, not a line.
#     double linePointDist(int[] A, int[] B, int[] C, boolean isSegment){
#         double dist = cross(A,B,C) / distance(A,B);
#         if(isSegment){
#             int dot1 = dot(A,B,C);
#             if(dot1 > 0)return distance(B,C);
#             int dot2 = dot(B,A,C);
#             if(dot2 > 0)return distance(A,C);
#         }
#         return abs(dist);
#     }
