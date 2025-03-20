def matrix_prod(A, B):
    n = len(A)
    # matriz n x n vacía
    C = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                C[i][j] += A[i][k] * B[k][j]
    return C
A = [[1,2], [3,4]]
B = [[5, 6], [7,8]]

C = matrix_prod(A, B)
print(C)