input=[
[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],
[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],
[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9],
[0,0,5,0,1,0,3,0,0]
]
# print(input)

input_transpose = list(zip(*input)) # for columnwise checks

def box(input,i,j):
    elems=[]
    for ii in range(i//3*3,(i//3+1)*3):
        for jj in range(j//3*3,(j//3+1)*3):
            elems.append(input[ii][jj])
    return elems

print(box(input,2,5))

choices = input[:]
choices_transpose = list(zip(*choices)) # for columnwise checks

for i in range(9):
    for j in range(9):
        if input[i][j]==0:
            # choices[i][j]=[x for x in range(1,10) if x not in input[i] and x not in input_transpose[j] and x not in box(input,i,j)]
            choices[i][j]=[x for x in range(1,10) if x not in choices[i] and x not in choices_transpose[j] and x not in box(choices,i,j)]
            if len(choices[i][j])==1:
                choices[i][j]=choices[i][j][0]
print(choices)

while any(isinstance(choices[i][j], list) for i in range(9) for j in range(9)):
    for i in range(9):
        for j in range(9):
            if isinstance(choices[i][j], list):
                # choices[i][j]=[x for x in range(1,10) if x not in input[i] and x not in input_transpose[j] and x not in box(input,i,j)]
                choices[i][j]=[x for x in range(1,10) if x not in choices[i] and x not in choices_transpose[j] and x not in box(choices,i,j)]
                if len(choices[i][j])==1:
                    choices[i][j]=choices[i][j][0]
                choices_transpose = list(zip(*choices)) # for columnwise checks
    print(choices)

print(choices)


# output
# [
# [4, 8, 3, 9, 2, 1, 6, 5, 7],
# [9, 6, 7, 3, 4, 5, 8, 2, 1],
# [2, 5, 1, 8, 7, 6, 4, 9, 3],
# [5, 4, 8, 1, 3, 2, 9, 7, 6],
# [7, 2, 9, 5, 6, 4, 1, 3, 8],
# [1, 3, 6, 7, 9, 8, 2, 4, 5],
# [3, 7, 2, 6, 8, 9, 5, 1, 4],
# [8, 1, 4, 2, 5, 3, 7, 6, 9],
# [6, 9, 5, 4, 1, 7, 3, 8, 2]
# ]
