def matrix_operation (M) :
    for i in range(0, len(M)) :
        for j in range(0, i) :
            M[i][j] = 0
    
    return M

M = [[9, 8, 3, 1], [3, 7, 5, 8], [2, 4, 6, 8], [1, 2, 3, 1]]

M = matrix_operation(M)

print(M)