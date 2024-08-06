
# matrix operation 
## matrix minor
def minor(A, i, j):
    return [row[:j] + row[j+1:] for row in (A[:i] + A[i+1:])]
## matrix multiplication
def matrix_multiplication(A, B):
    # check if the matrix can be multiplied
    if len(A[0]) != len(B):
        return "The matrix can't be multiplied"
    else:
        result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    
## matrix transpose
def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

## matrix determinant
def determinant(A):
    # check if the matrix is square
    if len(A) != len(A[0]):
        return "The matrix is not square"
    else:
        # check if the matrix is 2x2
        if len(A) == 2:
            return A[0][0] * A[1][1] - A[0][1] * A[1][0]
        else:
            result = 0
            for i in range(len(A)):
                result += ((-1)**i) * A[0][i] * determinant(minor(A, 0, i))
            return result
        
## matrix inversion
def matrix_inversion(A):
    # check if the matrix is square
    if len(A) != len(A[0]):
        return "The matrix is not square"
    else:
        # check if the matrix is invertible
        if determinant(A) == 0:
            return "The matrix is not invertible"
        else:
            # create the adjugate matrix
            adjugate = [[0 for i in range(len(A))] for j in range(len(A))]
            for i in range(len(A)):
                for j in range(len(A)):
                    adjugate[i][j] = ((-1)**(i+j)) * determinant(minor(A, i, j))
            # create the inverse matrix
            inverse = [[adjugate[i][j] / determinant(A) for j in range(len(A))] for i in range(len(A))]
            return inverse
            
## matrix eigenvalues
def matrix_eigenvalues(A):
    pass
## matrix eigenvectors
def matrix_eigenvectors(A):
    pass
## matrix norm
def norm(A):
    return max([sum([abs(A[i][j]) for j in range(len(A[0]))]) for i in range(len(A))])
## matrix distance
def distance(A, B):
    return norm([[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))])


## test 
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

print(minor(A, 1, 1))
print(matrix_multiplication(A, B))
print(transpose(A))
print(determinant(A))
print(matrix_inversion(A))
print(norm(A))
