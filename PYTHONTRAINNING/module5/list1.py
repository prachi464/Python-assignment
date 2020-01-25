#Nested list comprehnesion
matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)
print("\n")

matrix=[[j for j in range(5)]for i in range(5)]
print(matrix)
print("\n")
#flatter a given 2d list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
fl_mat=[1,2,3,4,5,6,7,8,9]


matrix=[[1,2,3],[4,5],[6,7,8,9]]
fl_mat=[]
for sublist in matrix:
    for val in sublist:
        fl_mat.append(val)
    print(fl_mat)

print("\n")
#nested list comprehnsion
fl_mat=[val for sublist in matrix for val in sublist]
print(fl_mat)
