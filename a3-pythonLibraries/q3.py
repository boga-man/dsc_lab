# program to compute the sum of two matrices
mat1 = []
mat2 = []

# get the dimensions of the lists from the user
rows = int(input("Enter the number of rows in the matrices: "))
cols = int(input("Enter the number of columns in the matrices: "))

# get the matrix 1
print("Enter the first matrix: ")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input("Enter element (" + str(i+1) + "," + str(j+1) + "): ")))
    mat1.append(row)

# get the matrix 2
print("Enter the second matrix: ")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input("Enter element (" + str(i+1) + "," + str(j+1) + "): ")))
    mat2.append(row)

# add the matrices
mat3 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(mat1[i][j] + mat2[i][j])
    mat3.append(row)

# print the matrices
print("Matrix 1:", mat1)
print("Matrix 2:", mat2)
print("The sum of the matrices is: ", mat3)